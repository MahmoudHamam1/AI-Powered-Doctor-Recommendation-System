# Test Cases for AI Doctor Recommendation System

## Test Case 1: Cardiology - Chest Pain
**Input Text:**
"I've been having severe chest pain and difficulty breathing for 3 days. The pain gets worse when I exercise and I feel dizzy."

**Expected Output:**
- Specialty: Cardiology
- Urgency: High
- Recommended Doctors: Dr. Michael Chen, Dr. Sarah Johnson

---

## Test Case 2: Dermatology - Skin Rash
**Input Text:**
"I have itchy red rashes on my arms and legs that won't go away. They're scaly and worse at night."

**Expected Output:**
- Specialty: Dermatology
- Urgency: Low to Medium
- Recommended Doctors: Dr. Emily Rodriguez, Dr. James Wilson

---

## Test Case 3: Orthopedics - Back Pain
**Input Text:**
"Severe lower back pain shooting down my right leg. Started after lifting heavy objects. Can't stand for long."

**Expected Output:**
- Specialty: Orthopedics
- Urgency: Medium
- Recommended Doctors: Dr. Maria Garcia, Dr. Robert Taylor

---

## Test Case 4: Neurology - Headaches
**Input Text:**
"Constant severe headaches with blurred vision and sensitivity to light. Having trouble concentrating."

**Expected Output:**
- Specialty: Neurology
- Urgency: High
- Recommended Doctors: Dr. Lisa Anderson, Dr. David Kim

---

## Test Case 5: Gastroenterology - Digestive Issues
**Input Text:**
"Persistent stomach pain, bloating, and irregular bowel movements for 2 weeks. Loss of appetite."

**Expected Output:**
- Specialty: Gastroenterology
- Urgency: Medium
- Recommended Doctors: Dr. Jennifer Lee, Dr. William Brown

---

## Test Case 6: Endocrinology - Diabetes Symptoms
**Input Text:**
"Excessive thirst, frequent urination, unexplained weight loss, and constant fatigue for the past month."

**Expected Output:**
- Specialty: Endocrinology
- Urgency: Medium to High
- Recommended Doctors: Dr. Amanda White, Dr. Christopher Davis

---

## Test Case 7: Pulmonology - Breathing Problems
**Input Text:**
"Chronic cough with wheezing, shortness of breath especially at night, and chest tightness."

**Expected Output:**
- Specialty: Pulmonology
- Urgency: Medium to High
- Recommended Doctors: Dr. Patricia Martinez, Dr. Daniel Thompson

---

## Price Preference Tests

### Low Price Preference
- Should prioritize doctors with lower consultation fees
- Still maintain reasonable quality (rating > 4.5)

### Medium Price Preference
- Balance between price and rating
- Default option for most users

### High Price Preference
- Prioritize highest-rated doctors
- Focus on experience and expertise

---

## File Upload Tests

### TXT File Test
- Use: `test_files/sample_health_record.txt`
- Contains: Cardiology case with chest pain

### PDF File Test
- Use: `test_files/dermatology_case.pdf`
- Contains: Dermatology consultation report

### DOCX File Test
- Use: `test_files/orthopedic_report.docx`
- Contains: Orthopedic back pain case

---

## Voice Input Test Phrases

1. "I have a persistent cough and fever"
2. "My joints are swollen and painful"
3. "I'm experiencing memory problems and confusion"
4. "Severe abdominal pain and nausea"
5. "Irregular heartbeat and chest discomfort"

## Test Case 8: Dentistry - Tooth Pain
**Input Text:**
"I have a severe toothache and my gums are swollen and bleeding. Need a dentist urgently."

**Expected Output:**
- Specialty: Dentistry
- Urgency: Low
- Recommended Doctors: Dr. Steven Park, Dr. Michelle Wong

---

## Test Case 9: Ophthalmology - Vision Problems
**Input Text:**
"My vision is blurry and I see floaters. Need an ophthalmologist."

**Expected Output:**
- Specialty: Ophthalmology
- Urgency: Medium
- Recommended Doctors: Dr. Kevin Foster, Dr. Laura Bennett

---

## Test Case 10: Psychiatry - Mental Health
**Input Text:**
"I have severe anxiety and depression. Need a psychiatrist for therapy."

**Expected Output:**
- Specialty: Psychiatry
- Urgency: Medium
- Recommended Doctors: Dr. Richard Stone, Dr. Angela Cruz

---

## Test Case 11: Urology - Urinary Issues
**Input Text:**
"I have frequent urination and bladder pain. Need a urologist."

**Expected Output:**
- Specialty: Urology
- Urgency: Medium
- Recommended Doctors: Dr. Brian Murphy

---

## Test Case 12: Gynecology - Women's Health
**Input Text:**
"I have irregular menstrual cycles and pelvic pain. Need a gynecologist."

**Expected Output:**
- Specialty: Gynecology
- Urgency: Medium
- Recommended Doctors: Dr. Sophia Turner

---
