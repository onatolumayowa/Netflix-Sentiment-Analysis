#!/bin/bash

echo "🔧 Creating virtual environment..."
python3 -m venv venv

echo "📂 Activating virtual environment..."
source venv/bin/activate

echo "⬇ Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Environment setup complete! 🎉"
echo "To activate next time, run: source venv/bin/activate"
