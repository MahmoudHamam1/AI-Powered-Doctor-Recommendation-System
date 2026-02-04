# AI Doctor Recommendation System

> A human-centered healthcare application using Google's Health AI models to match patients with the right doctors based on symptoms, ratings, and pricing.

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.53-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Overview

This application demonstrates a privacy-first approach to healthcare AI by providing intelligent doctor recommendations based on patient symptoms. Built for the Google Health AI Developer Foundations (HAI-DEF) challenge, it showcases how open-source models can be used to create practical, human-centered healthcare solutions.

## Architecture

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed system architecture diagram.

**Key Components:**
- **Input Layer**: Multi-modal input (text, voice, documents)
- **Processing Layer**: Document extraction and text preprocessing
- **AI Layer**: Gemma 2 2B model with rule-based fallback
- **Matching Layer**: Smart doctor recommendation engine
- **Output Layer**: Specialty detection, urgency assessment, doctor list

## Features

- **Text Input**: Describe symptoms in natural language
- **Voice Input**: Record symptoms via microphone (optional)
- **Document Upload**: Upload health records (PDF, DOCX, TXT)
- **AI Analysis**: Uses Gemma 2 2B with medical prompting
- **Smart Matching**: Recommends doctors by rating and price preference
- **Privacy-First**: Runs locally with open-source models
- **Security**: Input validation and prompt injection protection

## 🚀 Quick Start

```bash
# Clone the repository
git clone <your-repo-url>
cd med

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Setup

1. Install system dependencies (for voice input - optional):
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Install PyAudio for voice input:
```bash
pip install pyaudio
```

4. (Optional) For Gemma 2 2B model - Set up Hugging Face token:
```bash
export HF_TOKEN=your_huggingface_token
```

5. (Optional) Pre-download Gemma for offline use:
```bash
python download_model.py
```

6. Run the app:
```bash
streamlit run app.py
```

**Note:** The app works out-of-the-box with text input and document upload. Voice input and Gemma model are optional features.

## Usage

1. Choose input method (text, voice, or document)
2. Provide your symptoms or health information
3. Select price preference (low, medium, high)
4. Get AI-powered doctor recommendations

## Technology Stack

- **AI Model**: Gemma 2 2B IT (Open-source from Google)
- **Framework**: Transformers, PyTorch
- **Frontend**: Streamlit
- **Voice**: SpeechRecognition
- **Documents**: PyPDF2, python-docx

## Testing

Run unit tests:
```bash
python test_app.py
```

Sample test files are available in `test_files/` directory:
- `sample_health_record.txt` - Cardiology case
- `dermatology_case.txt` - Skin condition report
- `orthopedic_report.txt` - Back pain consultation
- `gastro_consultation.txt` - Digestive issues

See [TEST_CASES.md](TEST_CASES.md) for detailed test scenarios covering all 12+ specialties.

## About MedGemma & HAI-DEF

MedGemma is part of Google's Health AI Developer Foundations (HAI-DEF), designed for:
- Privacy-focused healthcare applications
- Local deployment without internet dependency
- Medical question answering and clinical decision support

**Note:** The app uses Gemma (Google's open LLM) with medical prompting. For production, you can fine-tune on medical data or use the rule-based system which works excellently for specialty detection.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⚠️ Disclaimer

**This application is for demonstration purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified health providers with any questions regarding medical conditions.**

## License

MIT License - see LICENSE file for details.

## Built For

Google Health AI Developer Foundations (HAI-DEF) Challenge - Building human-centered AI applications with open-source health models.
