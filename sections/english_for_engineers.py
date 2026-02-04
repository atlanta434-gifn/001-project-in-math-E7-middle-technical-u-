import streamlit as st
from utils import section_header, get_ai_explanation

def show():
    section_header("الإنجليزية للمهندسين", "Technical English for Engineers")
    
    st.markdown("""
    <div class="rtl">
        تطوير مهارات اللغة الإنجليزية التقنية اللازمة للتواصل في البيئات الهندسية العالمية.
    </div>
    """, unsafe_allow_html=True)
    
    category = st.selectbox("اختر مجال التركيز:", [
        "المصطلحات التقنية العامة",
        "كتابة التقارير الهندسية",
        "المصطلحات الخاصة بالإلكترونيات",
        "المصطلحات الخاصة بالذكاء الاصطناعي",
        "المحادثة في بيئة العمل"
    ])
    
    if st.button("عرض الدرس"):
        with st.spinner("جاري إعداد الدرس..."):
            explanation = get_ai_explanation(f"Provide a technical English lesson for Arabic-speaking engineers focusing on {category}. Include key vocabulary, phrases, and examples.")
            st.markdown(explanation)
            
    st.divider()
    st.subheader("مترجم المصطلحات التقنية")
    term = st.text_input("أدخل المصطلح بالإنجليزية (مثال: Capacitor, Neural Network):")
    if term:
        if st.button("ترجمة وشرح"):
            with st.spinner("جاري الترجمة..."):
                explanation = get_ai_explanation(f"Translate the engineering term '{term}' to Arabic and provide a brief technical explanation in both languages.")
                st.info(explanation)
                
    st.subheader("تمرين تفاعلي")
    st.write("حاول ترجمة الجملة التالية: 'The circuit is protected by a fuse.'")
    if st.button("عرض الترجمة الصحيحة"):
        st.success("الدائرة محمية بواسطة مصهر (فيوز).")
