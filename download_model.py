#!/usr/bin/env python3
"""
Pre-download MedGemma model for offline use
Run this once with internet connection
"""

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os
from dotenv import load_dotenv

load_dotenv()

print("🔽 Downloading MedGemma model...")
print("This will take 5-15 minutes depending on your connection.")
print("Model will be cached locally for offline use.\n")

model_name = "google/medgemma-1.1-2b-it"
token = os.getenv("HF_TOKEN")

try:
    print("📦 Downloading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_name, token=token)
    print("✅ Tokenizer downloaded\n")
    
    print("📦 Downloading model (~5GB)...")
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16,
        token=token
    )
    print("✅ Model downloaded\n")
    
    print("🎉 Success! MedGemma is now cached locally.")
    print(f"📁 Cache location: ~/.cache/huggingface/hub/")
    print("\n✨ You can now run the app offline!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nMake sure:")
    print("1. HF_TOKEN is set in .env file")
    print("2. You have internet connection")
    print("3. You have ~10GB free disk space")
