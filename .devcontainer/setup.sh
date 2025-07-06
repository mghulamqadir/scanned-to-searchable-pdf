#!/bin/bash

set -e

echo "🔧 Installing system packages..."
sudo apt update && sudo apt install -y \
  ghostscript \
  tesseract-ocr \
  libglib2.0-0 \
  libsm6 \
  libxrender1 \
  libxext6

echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🚀 Launching Streamlit..."
streamlit run main.py --server.enableCORS false --server.enableXsrfProtection false
