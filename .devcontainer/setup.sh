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

echo "✅ Installed ghostscript and tesseract"
echo "📍 Tesseract location: $(which tesseract)"
echo "📍 Adding to PATH if necessary"

# Optionally export to PATH (usually not needed but safe)
export PATH="/usr/bin:$PATH"

echo "📦 Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🚀 Ready to launch Streamlit (launch it manually or auto from devcontainer)"
