import streamlit as st
from utils import section_header, get_ai_explanation

def show():
    section_header("حساب التكامل", "التكامل المحدد وغير المحدد")
    
    equation = st.text_input("أدخل المعادلة للتكامل (مثال: 2x + 5):", "2x + 5")
    int_type = st.radio("نوع التكامل:", ["غير محدد (Indefinite)", "محدد (Definite)"], horizontal=True)
    
    if int_type == "محدد (Definite)":
        col1, col2 = st.columns(2)
        with col1: lower = st.number_input("الحد الأدنى:", value=0.0)
        with col2: upper = st.number_input("الحد الأعلى:", value=1.0)
        prompt = f"Calculate the definite integral of {equation} from {lower} to {upper}. Show steps."
    else:
        prompt = f"Calculate the indefinite integral of {equation}. Show steps."
        
    if st.button("تكامل"):
        with st.spinner("جاري الحساب..."):
            explanation = get_ai_explanation(prompt)
            st.markdown(explanation)
            
    st.divider()
    st.subheader("تطبيقات التكامل")
    st.write("استخدم التكامل لحساب المساحات والحجوم.")
    if st.button("شرح حساب المساحة تحت المنحنى"):
        with st.spinner("جاري الشرح..."):
            explanation = get_ai_explanation("Explain how to use integration to find the area under a curve with a simple example.")
            st.info(explanation)
