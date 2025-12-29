import streamlit as st
import requests

# st.title("Language Translator")

# text=st.text_area("Write your name")

# if st.button("Submit"):
#     if text:
#         response = requests.post(url="https://kpinno.app.n8n.cloud/webhook-test/bc95ff95-2880-4133-adbe-3c1ae89d6a85",json={"text":text})
        
#         if response.status_code == 200:
#             st.write(response.json()[0]["output"])
# else:
#     pass

# Page configuration
st.set_page_config(
    page_title="Language Translator",
    page_icon="🌐",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 0.5rem;
        border-radius: 10px;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .title-container {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .title-text {
        color: white;
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0;
    }
    .subtitle-text {
        color: #f0f0f0;
        font-size: 1.1rem;
        margin-top: 0.5rem;
    }
    .result-box {
        background-color: #f0f7ff;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
        margin-top: 1rem;
    }
    .info-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #ffc107;
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header with gradient background
st.markdown("""
    <div class="title-container">
        <h1 class="title-text">🌐 Language Translator</h1>
        <p class="subtitle-text">Translate your text to any language instantly</p>
    </div>
""", unsafe_allow_html=True)

# Info box
st.markdown("""
    <div class="info-box">
        <strong>ℹ️ How to use:</strong> Enter your text below, select your target language, and click Submit to translate!
    </div>
""", unsafe_allow_html=True)

# Create two columns for better layout
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📝 Enter Your Text")
    text = st.text_area("Write your text", height=150, placeholder="Type or paste your text here...")

with col2:
    st.markdown("### 🌍 Select Language")
    
    # Language options
    languages = {
        "Spanish": "es",
        "French": "fr",
        "German": "de",
        "Italian": "it",
        "Portuguese": "pt",
        "Russian": "ru",
        "Japanese": "ja",
        "Chinese (Simplified)": "zh-CN",
        "Korean": "ko",
        "Arabic": "ar",
        "Hindi": "hi",
        "Dutch": "nl",
        "Turkish": "tr",
        "Swedish": "sv",
        "Polish": "pl",
        "Hindi (हिन्दी)": "hi",
        "Bengali (বাংলা)": "bn",
        "Telugu (తెలుగు)": "te",
        "Marathi (मराठी)": "mr",
        "Tamil (தமிழ்)": "ta",
        "Gujarati (ગુજરાતી)": "gu",
        "Kannada (ಕನ್ನಡ)": "kn",
        "Malayalam (മലയാളം)": "ml",
        "Punjabi (ਪੰਜਾਬੀ)": "pa",
        "Odia (ଓଡ଼ିଆ)": "or",
        "Urdu (اردو)": "ur",
        "Sanskrit (संस्कृतम्)": "sa",
    }
    
    selected_language = st.selectbox(
        "Choose target language",
        options=list(languages.keys()),
        index=0
    )
    
    # Display selected language code
    st.info(f"Language Code: **{languages[selected_language]}**")

# Add some spacing
st.markdown("<br>", unsafe_allow_html=True)

# Submit button
if st.button("🚀 Translate Now"):
    if text:
        with st.spinner('🔄 Translating...'):
            try:
                # Modify the payload to include the target language
                payload = {
                    "text": text,
                    "target_language": languages[selected_language],
                    "language_name": selected_language
                }
                
                response = requests.post(
                    url="https://kpinno.app.n8n.cloud/webhook-test/bc95ff95-2880-4133-adbe-3c1ae89d6a85",
                    json=payload
                )
                
                if response.status_code == 200:
                    st.success("✅ Translation completed successfully!")
                    
                    # Display result in a styled box
                    st.markdown(f"""
                        <div class="result-box">
                            <h3 style="color: #2c3e50; margin-top: 0;">
                                📄 Translated Text ({selected_language}):
                            </h3>
                            <p style="font-size: 1.1rem; color: #34495e; line-height: 1.6;">
                                {response.json()[0]["output"]}
                            </p>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # Add download button for translated text
                    st.download_button(
                        label="💾 Download Translation",
                        data=response.json()[0]["output"],
                        file_name=f"translation_{selected_language}.txt",
                        mime="text/plain"
                    )
                else:
                    st.error(f"❌ Error: Received status code {response.status_code}")
                    
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
    else:
        st.warning("⚠️ Please enter some text to translate!")
else:
    pass

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #7f8c8d; padding: 1rem;">
        <p>Made with ❤️ using Streamlit | Powered by AI Translation</p>
    </div>""", unsafe_allow_html=True)