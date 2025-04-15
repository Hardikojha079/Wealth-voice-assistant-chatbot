# AI Voice Assistant for Wealth Management 💰🎙️🤖

## 🚀 Quick Start
This project is an AI-powered voice assistant designed specifically for wealth management and financial advisory services. It combines speech recognition, natural language processing, and text-to-speech technologies to provide interactive financial guidance through a voice interface.

## Key Features

```Voice Interaction:``` Users can ask financial questions via voice and receive spoken responses

```Financial Expertise:``` 

Specialized in wealth management topics including:

Investment strategies

Retirement planning

Tax optimization

Estate planning

Financial products comparison

```Intent Classification:``` Uses BERT model to understand user questions and categorize them

```LLM Integration:``` Falcon-RW-1B model generates detailed financial responses

```Text-to-Speech:``` Converts responses to natural sounding audio

```Unity Client:``` Mobile-friendly interface for recording and playback

## Technical Components

# Backend (Python/Flask)
```app.py:``` Main Flask server handling audio processing and response generation

```model_handler.py:``` Manages LLM and intent classification models

```tts_handler.py:``` Handles text-to-speech conversion

```train_classifier.py:``` Script for training the intent classifier

```predict.py:``` To predict modal queries for response verification

```augmented-banking-dataset.py:``` Generates training data with question variations

# Unity Client (C#)
```VoiceRecorder.cs:``` Handles microphone input and backend communication

```WavUtility.cs:``` Converts audio clips to WAV format

```MicrophonePermission.cs:``` Manages microphone permissions on Android

# Installation
Prerequisites 

```Python 3.8+```

```Unity 2021.3+```

```NVIDIA GPU (recommended for faster inference)```

# Sample Questions

"What's the difference between stocks and bonds?"

"How much should I save for retirement?"

"Explain dollar-cost averaging"

"What is a Roth IRA?"

"How do capital gains taxes work?"

```bash
# Clone the repository
git clone https://github.com/Hardikojha079/Wealth-voice-assistant-chatbot.git
cd wealth-voice-assistant

# Set up Python virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows

# Install backend dependencies
pip install -r requirements.txt

# Download models (ensure you have git-lfs installed)
git lfs install
git clone https://huggingface.co/tiiuae/falcon-rw-1b models/falcon-rw-1b

# Generating training data with question variations
python augmented-bank-dataset.py

# Training model
python train_classifier.py

#Performing prediction for response verification
python predict.py

# Start the Flask backend server
python app.py

wealth-voice-assistant/
├── backend/               # Python Flask server
│   ├── app.py             # Main application
│   ├── model_handler.py   # LLM and classifier
│   ├── tts_handler.py     # Text-to-speech
│   └── requirements.txt   # Dependencies
├── unity-client/          # Unity project
│   ├── Assets/
│   │   ├── Scripts/
│   │   │   ├── VoiceRecorder.cs
│   │   │   └── WavUtility.cs
│   └── ProjectSettings/
└── models/                # AI models
    ├── falcon-rw-1b/      # Language model
    └── bert_banking_classifier/  # Intent classifier
```
# Architecture

```User Voice Input → Unity Client → Flask Backend → Speech Recognition → ```

```Intent Classification → LLM Response Generation → Text-to-Speech →```

```Audio Response → Unity Client → Playback```

# Future Enhancements

Add multi-language support

Implement user authentication for personalized advice

Integrate with financial APIs for real-time data

Add follow-up question handling

Improve error handling and fallback responses

