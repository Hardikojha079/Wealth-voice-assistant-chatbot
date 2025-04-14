# AI Voice Assistant for Wealth Management 💰🎙️🤖

![Project Banner](https://via.placeholder.com/800x200?text=AI+Wealth+Management+Voice+Assistant)

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/wealth-voice-assistant.git
cd wealth-voice-assistant

# Set up Python virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install backend dependencies
pip install -r requirements.txt

# Download models (ensure you have git-lfs installed)
git lfs install
git clone https://huggingface.co/tiiuae/falcon-rw-1b models/falcon-rw-1b

# Start the Flask backend server
python app.py
