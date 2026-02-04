import streamlit as st
from utils import section_header, get_ai_explanation

def show():
    section_header("الفيزياء الكمية", "ميكانيكا الكم وتطبيقاتها الحديثة")
    
    st.markdown("""
    <div class="rtl">
        فهم القوانين التي تحكم العالم على المستوى الذري ودون الذري.
    </div>
    """, unsafe_allow_html=True)
    
    topic = st.selectbox("اختر موضوعاً:", [
        "مبدأ عدم اليقين لهايزنبرغ",
        "معادلة شرودنغر",
        "الازدواجية موجة-جسيم",
        "النفق الكمي (Quantum Tunneling)",
        "النقاط الكمية (Quantum Dots)"
    ])
    
    if st.button("شرح الموضوع"):
        with st.spinner("جاري جلب الشرح..."):
            explanation = get_ai_explanation(f"Explain the concept of {topic} in quantum physics. Why is it fundamental to modern electronics and nanotechnology?")
            st.markdown(explanation)
            
    st.divider()
    st.subheader("لماذا ندرس الفيزياء الكمية؟")
    st.write("استكشف كيف غيرت ميكانيكا الكم حياتنا اليومية.")
    if st.button("أمثلة من الواقع"):
        with st.spinner("جاري التحليل..."):
            explanation = get_ai_explanation("Provide real-world examples of technologies that rely on quantum physics (e.g., MRI, Lasers, Transistors).")
            st.info(explanation)
