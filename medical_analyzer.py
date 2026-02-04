from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os
from dotenv import load_dotenv

load_dotenv()

class MedicalAnalyzer:
    def __init__(self):
        try:
            # Try to load Gemma 2 2B from Hugging Face
            model_name = "google/gemma-2-2b-it"
            print("Loading Gemma 2 2B model...")
            self.tokenizer = AutoTokenizer.from_pretrained(model_name, token=os.getenv("HF_TOKEN"))
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name, 
                torch_dtype=torch.float16, 
                device_map="auto",
                token=os.getenv("HF_TOKEN")
            )
            print("Gemma 2 2B loaded successfully!")
        except Exception as e:
            print(f"Could not load Gemma: {e}")
            print("Using rule-based fallback...")
            self.model = None
    
    def analyze_symptoms(self, text):
        # Basic input validation and sanitization
        if not text or len(text.strip()) < 5:
            return {"specialty": "General Medicine", "urgency": "Low", "summary": "Insufficient information provided"}
        
        # Limit input length to prevent abuse
        if len(text) > 5000:
            text = text[:5000]
        
        # Remove potential prompt injection attempts
        text = self._sanitize_input(text)
        
        if self.model:
            return self._analyze_with_model(text)
        else:
            return self._analyze_with_rules(text)
    
    def _sanitize_input(self, text):
        """Remove potential prompt injection patterns"""
        # Remove common prompt injection keywords
        dangerous_patterns = [
            "ignore previous instructions",
            "ignore all previous",
            "disregard",
            "forget everything",
            "new instructions",
            "system:",
            "assistant:",
            "<|im_start|>",
            "<|im_end|>",
        ]
        
        text_lower = text.lower()
        for pattern in dangerous_patterns:
            if pattern in text_lower:
                # Log potential attack
                print(f"[Security] Potential prompt injection detected: {pattern}")
                # Remove the pattern
                text = text.replace(pattern, "")
                text = text.replace(pattern.upper(), "")
                text = text.replace(pattern.title(), "")
        
        return text.strip()
    
    def _analyze_with_model(self, text):
        # Additional safety: Ensure text doesn't contain prompt delimiters
        text = text.replace("```", "").replace("###", "")
        
        prompt = f"""Analyze the following medical information and identify:
1. Primary medical specialty needed (e.g., Cardiology, Dermatology, Neurology, Orthopedics, Gastroenterology, Endocrinology, Pulmonology, Rheumatology, Dentistry, Ophthalmology, Psychiatry, Urology, Gynecology)
2. Urgency level (Low, Medium, High)
3. Brief summary of the condition

Patient input: {text}

Respond in this exact format:
SPECIALTY: [specialty name]
URGENCY: [urgency level]
SUMMARY: [brief summary]"""
        
        inputs = self.tokenizer(prompt, return_tensors="pt", max_length=1024, truncation=True).to(self.model.device)
        outputs = self.model.generate(**inputs, max_new_tokens=200, temperature=0.7, do_sample=True)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        print("\n" + "="*50)
        print("MODEL OUTPUT:")
        print("="*50)
        print(response)
        print("="*50 + "\n")
        
        return self._parse_response(response)
    
    def _analyze_with_rules(self, text):
        text_lower = text.lower()
        
        print(f"\n[Rule-based Analysis] Input: {text[:100]}...")
        
        # Check all specialties with expanded keywords
        if any(word in text_lower for word in ['tooth', 'teeth', 'dental', 'dentist', 'gum', 'cavity', 'toothache', 'molar', 'filling', 'crown', 'root canal']):
            result = {"specialty": "Dentistry", "urgency": "Low", "summary": "Dental issue detected"}
        elif any(word in text_lower for word in ['chest pain', 'heart', 'cardiac', 'cardiology', 'blood pressure', 'palpitation', 'cardiovascular', 'angina']):
            result = {"specialty": "Cardiology", "urgency": "High", "summary": "Cardiovascular symptoms detected"}
        elif any(word in text_lower for word in ['rash', 'skin', 'itch', 'acne', 'dermatitis', 'dermatology', 'eczema', 'psoriasis', 'melanoma']):
            result = {"specialty": "Dermatology", "urgency": "Low", "summary": "Skin condition detected"}
        elif any(word in text_lower for word in ['back pain', 'joint', 'bone', 'fracture', 'orthopedic', 'orthopedics', 'spine', 'arthritis', 'ligament']):
            result = {"specialty": "Orthopedics", "urgency": "Medium", "summary": "Musculoskeletal issue detected"}
        elif any(word in text_lower for word in ['headache', 'migraine', 'seizure', 'neurological', 'neurology', 'memory', 'stroke', 'epilepsy', 'brain']):
            result = {"specialty": "Neurology", "urgency": "High", "summary": "Neurological symptoms detected"}
        elif any(word in text_lower for word in ['stomach', 'abdominal', 'digestive', 'bowel', 'nausea', 'gastro', 'gastroenterology', 'intestine', 'diarrhea', 'constipation']):
            result = {"specialty": "Gastroenterology", "urgency": "Medium", "summary": "Digestive system issue detected"}
        elif any(word in text_lower for word in ['diabetes', 'thyroid', 'hormone', 'endocrine', 'endocrinology', 'insulin', 'glucose', 'metabolic']):
            result = {"specialty": "Endocrinology", "urgency": "Medium", "summary": "Endocrine condition detected"}
        elif any(word in text_lower for word in ['breathing', 'cough', 'lung', 'asthma', 'respiratory', 'pulmonology', 'bronchitis', 'pneumonia', 'copd']):
            result = {"specialty": "Pulmonology", "urgency": "High", "summary": "Respiratory symptoms detected"}
        elif any(word in text_lower for word in ['eye', 'vision', 'sight', 'blurry', 'ophthalmology', 'ophthalmologist', 'cataract', 'glaucoma', 'retina']):
            result = {"specialty": "Ophthalmology", "urgency": "Medium", "summary": "Eye/vision issue detected"}
        elif any(word in text_lower for word in ['anxiety', 'depression', 'mental', 'psychiatric', 'psychiatry', 'stress', 'bipolar', 'schizophrenia', 'therapy']):
            result = {"specialty": "Psychiatry", "urgency": "Medium", "summary": "Mental health concern detected"}
        elif any(word in text_lower for word in ['urinary', 'bladder', 'kidney', 'urology', 'urologist', 'prostate', 'uti', 'incontinence']):
            result = {"specialty": "Urology", "urgency": "Medium", "summary": "Urological issue detected"}
        elif any(word in text_lower for word in ['pregnancy', 'menstrual', 'gynecology', 'gynecologist', 'ovarian', 'uterus', 'pelvic', 'cervical', 'obstetric']):
            result = {"specialty": "Gynecology", "urgency": "Medium", "summary": "Gynecological concern detected"}
        else:
            result = {"specialty": "General Medicine", "urgency": "Medium", "summary": "General medical consultation needed"}
        
        print(f"[Rule-based Analysis] Result: {result}\n")
        return result
    
    def _parse_response(self, text):
        lines = text.strip().split('\n')
        result = {"specialty": "", "urgency": "", "summary": ""}
        
        for line in lines:
            if "SPECIALTY:" in line:
                specialty = line.split("SPECIALTY:")[-1].strip()
                # Remove markdown formatting
                specialty = specialty.replace("**", "").replace("*", "").strip()
                result["specialty"] = specialty
            elif "URGENCY:" in line:
                urgency = line.split("URGENCY:")[-1].strip()
                urgency = urgency.replace("**", "").replace("*", "").strip()
                result["urgency"] = urgency
            elif "SUMMARY:" in line:
                summary = line.split("SUMMARY:")[-1].strip()
                summary = summary.replace("**", "").replace("*", "").strip()
                result["summary"] = summary
        
        return result
