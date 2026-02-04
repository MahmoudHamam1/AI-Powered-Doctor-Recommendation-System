import streamlit as st
from medical_analyzer import MedicalAnalyzer
from doctor_matcher import DoctorMatcher
from document_processor import DocumentProcessor

st.set_page_config(page_title="AI Doctor Finder", page_icon="🏥", layout="wide")

st.title("🏥 AI-Powered Doctor Recommendation System")
st.markdown("*Powered by MedGemma & Google Health AI*")

# Add custom CSS for clickable buttons
st.markdown("""
<style>
.book-btn {
    background-color: transparent;
    color: #28a745;
    border: 2px solid #28a745;
    padding: 8px 16px;
    border-radius: 5px;
    text-align: center;
    cursor: pointer;
    font-weight: bold;
    transition: all 0.3s;
    display: inline-block;
}
.book-btn:hover {
    background-color: #28a745;
    color: white;
}
button[kind="secondary"] {
    background-color: transparent !important;
    color: #28a745 !important;
    border: 2px solid #28a745 !important;
}
button[kind="secondary"]:hover {
    background-color: #28a745 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

if 'analyzer' not in st.session_state:
    st.session_state.analyzer = MedicalAnalyzer()
    st.session_state.matcher = DoctorMatcher()
    st.session_state.processor = DocumentProcessor()

tab1, tab2, tab3 = st.tabs(["📝 Text Input", "🎤 Voice Input", "📄 Upload Records"])

with tab1:
    st.subheader("Describe your symptoms or medical concern")
    text_input = st.text_area("Enter your symptoms:", height=150)
    
    col1, col2 = st.columns(2)
    with col1:
        price_pref = st.selectbox("Price Preference:", ["low", "medium", "high"])
    with col2:
        analyze_btn = st.button("Find Doctors", type="primary")
    
    if analyze_btn and text_input:
        with st.spinner("Analyzing your symptoms..."):
            analysis = st.session_state.analyzer.analyze_symptoms(text_input)
            
            with st.expander("🔍 View AI Model Output", expanded=False):
                st.json(analysis)
            
            st.success(f"**Recommended Specialty:** {analysis['specialty']}")
            st.info(f"**Summary:** {analysis['summary']}")
            st.warning(f"**Urgency:** {analysis['urgency']}")
            
            doctors = st.session_state.matcher.find_doctors(analysis['specialty'], price_pref)
            
            st.subheader("🩺 Recommended Doctors")
            for i, doc in enumerate(doctors, 1):
                with st.container():
                    col1, col2, col3, col4 = st.columns([3, 2, 1, 1])
                    with col1:
                        st.markdown(f"**{i}. {doc['name']}**")
                        st.caption(f"{doc['specialty']} • {doc['experience']} years exp")
                    with col2:
                        st.metric("Rating", f"⭐ {doc['rating']}")
                    with col3:
                        st.metric("Price", f"${doc['price']}")
                    with col4:
                        st.markdown(f'<div class="book-btn">✅ Book</div>', unsafe_allow_html=True)
                    st.divider()

with tab2:
    st.subheader("Record your symptoms")
    st.info("💡 Voice input requires PyAudio. Install with: `sudo apt-get install portaudio19-dev && pip install pyaudio`")
    
    try:
        import speech_recognition as sr
        
        if st.button("🎤 Start Recording"):
            recognizer = sr.Recognizer()
            with st.spinner("Listening..."):
                try:
                    with sr.Microphone() as source:
                        audio = recognizer.listen(source, timeout=5)
                        text = recognizer.recognize_google(audio)
                        st.session_state.voice_text = text
                        st.success(f"Recognized: {text}")
                except Exception as e:
                    st.error(f"Could not recognize speech: {e}")
        
        if 'voice_text' in st.session_state:
            price_pref_voice = st.selectbox("Price Preference:", ["low", "medium", "high"], key="voice_price")
            
            if st.button("Analyze Voice Input", type="primary"):
                with st.spinner("Analyzing..."):
                    analysis = st.session_state.analyzer.analyze_symptoms(st.session_state.voice_text)
                    
                    with st.expander("🔍 View AI Model Output", expanded=False):
                        st.json(analysis)
                    
                    st.success(f"**Recommended Specialty:** {analysis['specialty']}")
                    st.info(f"**Summary:** {analysis['summary']}")
                    
                    doctors = st.session_state.matcher.find_doctors(analysis['specialty'], price_pref_voice)
                    
                    st.subheader("🩺 Recommended Doctors")
                    for i, doc in enumerate(doctors, 1):
                        col1, col2 = st.columns([4, 1])
                        with col1:
                            st.markdown(f"**{i}. {doc['name']}** - {doc['specialty']} | ⭐ {doc['rating']} | ${doc['price']}")
                        with col2:
                            st.markdown(f'<div class="book-btn">✅ Book</div>', unsafe_allow_html=True)
    except ImportError:
        st.warning("⚠️ Voice input not available. PyAudio is not installed.")
        st.markdown("**Alternative:** Use text input or upload a document instead.")

with tab3:
    st.subheader("Upload your health records")
    uploaded_file = st.file_uploader("Choose a file (PDF, DOCX, TXT)", type=['pdf', 'docx', 'txt'])
    
    if uploaded_file:
        with st.spinner("Processing document..."):
            text = st.session_state.processor.extract_text(uploaded_file)
            if not text or len(text.strip()) < 10:
                st.error("Could not extract text from document. Please try another file.")
            else:
                st.text_area("Extracted Text:", text[:500] + "...", height=150)
        
        price_pref_doc = st.selectbox("Price Preference:", ["low", "medium", "high"], key="doc_price")
        
        if st.button("Analyze Document", type="primary") and text and len(text.strip()) >= 10:
            with st.spinner("Analyzing..."):
                analysis = st.session_state.analyzer.analyze_symptoms(text)
                
                with st.expander("🔍 View AI Model Output", expanded=False):
                    st.json(analysis)
                
                st.success(f"**Recommended Specialty:** {analysis['specialty']}")
                st.info(f"**Summary:** {analysis['summary']}")
                
                doctors = st.session_state.matcher.find_doctors(analysis['specialty'], price_pref_doc)
                
                st.subheader("🩺 Recommended Doctors")
                for i, doc in enumerate(doctors, 1):
                    with st.container():
                        col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
                        with col1:
                            st.markdown(f"**{i}. {doc['name']}**")
                            st.caption(f"{doc['specialty']}")
                        with col2:
                            st.metric("Rating", f"⭐ {doc['rating']}")
                        with col3:
                            st.metric("Price", f"${doc['price']}")
                        with col4:
                            st.markdown(f'<div class="book-btn">✅ Book</div>', unsafe_allow_html=True)
                        st.divider()

st.sidebar.title("About")
st.sidebar.info("""
This AI-powered system uses **MedGemma** (Google's open-source Health AI) to:
- Analyze symptoms from text, voice, or documents
- Identify the right medical specialty
- Recommend doctors based on ratings and pricing

🔒 **Privacy-First**: Runs locally, no data sent to cloud
""")

st.sidebar.markdown("---")
st.sidebar.markdown("**Supported Specialties:**")
st.sidebar.caption("Cardiology • Dermatology • Neurology • Orthopedics • Gastroenterology • Endocrinology • Pulmonology • Dentistry • Ophthalmology • Psychiatry • Urology • Gynecology")
