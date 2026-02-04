import streamlit as st
from utils import section_header, get_ai_explanation

def show():
    section_header("أساسيات الرياضيات والفيزياء", "المفاهيم الجوهرية للهندسة")
    
    st.markdown("""
    <div class="rtl">
        مراجعة للمفاهيم الأساسية التي يحتاجها كل مهندس في مسيرته الدراسية.
    </div>
    """, unsafe_allow_html=True)
    
    category = st.radio("اختر المجال:", ["الفيزياء الكلاسيكية", "الرياضيات الأساسية", "وحدات القياس"], horizontal=True)
    
    if category == "الفيزياء الكلاسيكية":
        topic = st.selectbox("الموضوع:", ["قوانين نيوتن", "الطاقة والشغل", "الكهرومغناطيسية"])
    elif category == "الرياضيات الأساسية":
        topic = st.selectbox("الموضوع:", ["المثلثات", "الأعداد المركبة", "المصفوفات"])
    else:
        topic = st.selectbox("الموضوع:", ["النظام الدولي للوحدات SI", "التحويل بين الوحدات"])
        
    if st.button("شرح المفهوم"):
        with st.spinner("جاري جلب المعلومات..."):
            explanation = get_ai_explanation(f"Explain the fundamental concept of {topic} in {category}. Provide examples and formulas.")
            st.markdown(explanation)
            
    st.divider()
    st.subheader("اختبر معلوماتك")
    st.write("سؤال سريع: ما هي وحدة قياس الفيض المغناطيسي؟")
    if st.button("إظهار الإجابة"):
        st.success("الويبر (Weber)")
