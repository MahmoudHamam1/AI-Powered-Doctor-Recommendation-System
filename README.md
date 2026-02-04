# AI-Powered Doctor Recommendation System

> Intelligent healthcare matching using Google's Gemma 2 AI to connect patients with the right specialists based on symptoms, ratings, and budget preferences.

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.53-red.svg)](https://streamlit.io/)
[![Gemma](https://img.shields.io/badge/Gemma-2B--IT-orange.svg)](https://huggingface.co/google/gemma-2-2b-it)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Overview

A privacy-first healthcare application that analyzes patient symptoms and recommends qualified doctors across 12+ medical specialties. Built for the **Google Health AI Developer Foundations (HAI-DEF)** challenge, this system demonstrates how open-source AI models can create practical, human-centered healthcare solutions.

**Key Highlights:**
- **Privacy-First**: Runs locally with no data sent to external servers
- **AI-Powered**: Gemma 2 2B model with intelligent rule-based fallback
- **Smart Matching**: Filters doctors by specialty, rating, and price preference
- **Multi-Modal Input**: Text, voice, and document upload support
- **Secure**: Built-in prompt injection protection and input validation

## Features

### Input Methods
- **Text Input**: Describe symptoms in natural language
- **Voice Input**: Record symptoms via microphone (optional)
- **Document Upload**: Upload health records (PDF, DOCX, TXT)

### AI Analysis
- **Gemma 2 2B Model**: Google's open-source LLM with medical prompting
- **Rule-Based Fallback**: Robust keyword matching for 12+ specialties
- **Specialty Detection**: Cardiology, Dermatology, Neurology, Orthopedics, and more
- **Urgency Assessment**: Identifies critical symptoms requiring immediate attention

### Doctor Matching
- **Rating-Based Sorting**: Find top-rated specialists
- **Price Filtering**: Low, medium, or high budget options
- **Comprehensive Database**: 25+ doctors across all major specialties

### Security & Privacy
- **Local Processing**: All data stays on your machine
- **Input Validation**: 5-5000 character limits with sanitization
- **Prompt Injection Protection**: Filters malicious input patterns

## Architecture

```
Input Layer → Processing Layer → AI Analysis → Doctor Matching → Results
(Text/Voice/Doc) → (Extract/Clean) → (Gemma/Rules) → (Filter/Sort) → (Display)
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed system architecture diagram with data flow.

## Quick Start

### Basic Setup (Works Immediately)

```bash
# Clone the repository
git clone https://github.com/MahmoudHamam1/AI-Powered-Doctor-Recommendation-System.git
cd AI-Powered-Doctor-Recommendation-System

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The app opens at `http://localhost:8501` and works immediately with text input and document upload using the rule-based system.

### Optional: Enable AI Model

To use Gemma 2 2B model for enhanced analysis:

```bash
# 1. Get Hugging Face token from https://huggingface.co/settings/tokens
# 2. Create .env file
echo "HF_TOKEN=your_huggingface_token" > .env

# 3. Pre-download model (optional, for offline use)
python download_model.py
```

### Optional: Enable Voice Input

```bash
# Install system dependencies (Ubuntu/Debian)
sudo apt-get install portaudio19-dev python3-pyaudio

# Install PyAudio
pip install pyaudio
```

## Usage

1. **Select Input Method**: Choose from text, voice, or document upload tabs
2. **Describe Symptoms**: Enter your health concerns or upload medical records
3. **Set Budget**: Select price preference (Low: $50-100, Medium: $100-150, High: $150-200)
4. **Get Recommendations**: View matched doctors with ratings, specialties, and contact info

### Example Queries
- "I have chest pain and shortness of breath" → Cardiology specialists
- "Skin rash with itching" → Dermatology experts
- "Severe headache and dizziness" → Neurology doctors
- Upload lab report → Specialty auto-detected from document

## Technology Stack

| Component | Technology |
|-----------|------------|
| **AI Model** | Gemma 2 2B IT (Google) |
| **ML Framework** | Transformers, PyTorch |
| **Frontend** | Streamlit |
| **Voice Processing** | SpeechRecognition |
| **Document Parsing** | PyPDF2, python-docx |
| **Language** | Python 3.12 |

## Project Structure

```
.
├── app.py                    # Main Streamlit application
├── medical_analyzer.py       # AI analysis with Gemma 2 2B
├── doctor_matcher.py         # Doctor recommendation engine
├── doctors_db.py             # Doctor database (25+ specialists)
├── document_processor.py     # PDF/DOCX/TXT extraction
├── download_model.py         # Model pre-download script
├── test_app.py              # Unit tests
├── test_files/              # Sample health records
├── requirements.txt         # Python dependencies
├── ARCHITECTURE.md          # System architecture diagram
└── TEST_CASES.md           # Comprehensive test scenarios
```

## Testing

```bash
# Run unit tests
python test_app.py
```

**Sample Test Files** (`test_files/` directory):
- `sample_health_record.txt` - Cardiology case (chest pain)
- `dermatology_case.txt` - Skin condition (eczema)
- `orthopedic_report.txt` - Back pain consultation
- `gastro_consultation.txt` - Digestive issues

See [TEST_CASES.md](TEST_CASES.md) for 12+ specialty test scenarios with expected outputs.

## About HAI-DEF Challenge

This project is built for **Google's Health AI Developer Foundations (HAI-DEF)** challenge, which promotes:
- Privacy-focused healthcare applications
- Local deployment without internet dependency
- Medical question answering and clinical decision support
- Human-centered AI design principles

**Model Choice**: Uses Gemma 2 2B IT (Google's open LLM) with medical prompting. The robust rule-based fallback ensures 100% uptime even without model access.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚠️ Disclaimer

**This application is for demonstration purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified health providers with any questions regarding medical conditions.**

## License

MIT License - see LICENSE file for details.

## Built For

**Google Health AI Developer Foundations (HAI-DEF) Challenge**  
Building human-centered AI applications with open-source health models.

