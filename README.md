# 🌐 Multi-Language Translator with Audio

A simple Streamlit app that translates between Bangla, English, and Hindi with Text-to-Speech functionality.

https://github.com/user-attachments/assets/57ba500e-f7da-4f2c-bfbb-41bad4a385e8

## Features
- **Translation Support**: 
  - Bangla → English
  - English → Hindi
  - Hindi → English
- **Audio Generation**: Text-to-Speech for translated text
- **Web Interface**: Clean and user-friendly interface

## � Quick Start

### Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app:**
   ```bash
   streamlit run main.py
   ```

3. **Open your browser:**
   Go to `http://localhost:8501`

### Docker Deployment

1. **Build and run:**
   ```bash
   docker build -t translator-app .
   docker run -p 8501:8501 translator-app
   ```

2. **Access the app:**
   Open `http://localhost:8501`

## 📦 Dependencies

- `transformers` - Translation models
- `streamlit` - Web framework  
- `torch` - Model inference
- `sentencepiece` - Tokenization
- `gtts` - Text-to-Speech

## � How to Use

1. Select translation direction
2. Enter your text
3. Click "Translate & Generate Audio 🔊"
4. Read the translation and listen to the audio
