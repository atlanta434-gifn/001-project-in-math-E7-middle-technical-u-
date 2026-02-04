import streamlit as st
from utils import section_header, get_ai_explanation

def show():
    section_header("أساسيات الكم والفوتونيات", "الضوء، الفوتونات، والتكنولوجيا الكمية")
    
    st.markdown("""
    <div class="rtl">
        استكشف عالم الفوتونيات وكيفية التحكم في الضوء على المستوى الكمي.
    </div>
    """, unsafe_allow_html=True)
    
    topic = st.selectbox("اختر موضوعاً:", [
        "طبيعة الضوء (موجة أم جسيم؟)",
        "الفوتونات والكيوبتات الضوئية",
        "الليزر وتطبيقاته",
        "الألياف البصرية",
        "المستشعرات الكمية"
    ])
    
    if st.button("شرح المفهوم"):
        with st.spinner("جاري جلب المعلومات..."):
            explanation = get_ai_explanation(f"Explain the concept of {topic} in the context of Quantum and Photonics. Why is it important for future engineering?")
            st.markdown(explanation)
            
    st.divider()
    st.subheader("تطبيقات عملية")
    st.write("كيف تساهم الفوتونيات في تسريع الإنترنت؟")
    if st.button("اكتشف الإجابة"):
        with st.spinner("جاري التحليل..."):
            explanation = get_ai_explanation("Explain the role of photonics and optical fibers in modern high-speed internet communication.")
            st.success(explanation)
