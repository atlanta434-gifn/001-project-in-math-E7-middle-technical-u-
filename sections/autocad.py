import streamlit as st
from utils import section_header, get_ai_explanation

def show():
    section_header("الرسم الهندسي (AutoCAD)", "تعلم مهارات التصميم بمساعدة الحاسوب")
    
    st.markdown("""
    <div class="rtl">
        دليل شامل لتعلم برنامج الأوتوكاد من البداية وحتى الاحتراف.
    </div>
    """, unsafe_allow_html=True)
    
    level = st.select_slider("اختر مستوى التعلم:", options=["مبتدئ", "متوسط", "متقدم"])
    
    topic = st.selectbox("اختر موضوعاً:", [
        "واجهة البرنامج والأوامر الأساسية",
        "الرسم ثنائي الأبعاد (2D Drafting)",
        "الطبقات (Layers) والألوان",
        "الأبعاد والنصوص (Dimensions & Text)",
        "النمذجة ثلاثية الأبعاد (3D Modeling)",
        "إعداد اللوحات للطباعة"
    ])
    
    if st.button("عرض الدرس"):
        with st.spinner("جاري إعداد المحتوى التعليمي..."):
            explanation = get_ai_explanation(f"Provide a tutorial for AutoCAD at {level} level focusing on {topic}. Include common commands and tips.")
            st.markdown(explanation)
            
    st.divider()
    st.subheader("قاموس أوامر AutoCAD")
    cmd = st.text_input("أدخل اسم الأمر (مثال: LINE, CIRCLE, TRIM):")
    if cmd:
        if st.button("شرح الأمر"):
            with st.spinner("جاري البحث..."):
                explanation = get_ai_explanation(f"Explain the AutoCAD command: {cmd}. How to use it and what are its options?")
                st.info(explanation)
