from transformers import MarianMTModel, MarianTokenizer
import streamlit as st
from gtts import gTTS
import io

st.title("🌐 Multi-Language Translator")

@st.cache_resource
def translate_model(direction):
    map={
        "Bangla to English": "Helsinki-NLP/opus-mt-bn-en",
        #"English to Bangla": "Helsinki-NLP/opus-mt-en-bn",
        "English to Hindi": "Helsinki-NLP/opus-mt-en-hi",
        "Hindi to English": "Helsinki-NLP/opus-mt-hi-en"
    }
    model_name = map[direction]
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

def generate_audio(text, language):
    """Generate audio from text using gTTS"""
    try:
        # Language mapping for gTTS
        lang_map = {
            "English": "en",
            "Hindi": "hi", 
            "Bangla": "bn"
        }
        
        tts = gTTS(text=text, lang=lang_map.get(language, "en"), slow=False)
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        return audio_buffer
    except Exception as e:
        st.error(f"Audio generation failed: {str(e)}")
        return None

direction = st.selectbox("Choose translation direction:", ["Bangla to English", "English to Hindi", "Hindi to English"])

if direction == "Bangla to English":
    placeholder = "Enter Bangla text"
elif direction == "English to Hindi":
    placeholder = "Enter English text"
else:  # Hindi to English
    placeholder = "Enter Hindi text"

user_text = st.text_area(f"✍️ {placeholder}:", "")

if st.button("Translate & Generate Audio 🔊"):
    if user_text.strip():
        with st.spinner("Translating and generating audio..."):
            try:
                tokenizer, model = translate_model(direction)
                
                inputs = tokenizer(user_text, return_tensors="pt", padding=True)
                translate = model.generate(**inputs)
                translated_text = tokenizer.decode(translate[0], skip_special_tokens=True)
                
                st.success(f"📝 Translated Text: {translated_text}")
                
                # Determine target language for audio
                if direction == "Bangla to English":
                    target_lang = "English"
                elif direction == "English to Hindi":
                    target_lang = "Hindi"
                elif direction == "Hindi to English":
                    target_lang = "English"
                else:
                    target_lang = "English"  # fallback
                
                # Generate and play audio
                audio_buffer = generate_audio(translated_text, target_lang)
                if audio_buffer:
                    st.audio(audio_buffer.read())
                    
            except Exception as e:
                st.error(f"Translation failed: {str(e)}")
    else:
        st.warning("❗ Please enter some text.")


            
