import streamlit as st
from utils import section_header, get_ai_explanation

def show():
    section_header("حساب التفاضل", "المشتقات وتطبيقاتها")
    
    equation = st.text_input("أدخل المعادلة للتفاضل (مثال: x^3 + 2x^2 + 5):", "x^3 + 2x^2 + 5")
    
    if st.button("اشتقاق"):
        with st.spinner("جاري الحساب..."):
            explanation = get_ai_explanation(f"Find the derivative of {equation} with respect to x. Provide a step-by-step solution and explain the rules used.")
            st.markdown(explanation)
            
    st.divider()
    st.subheader("تطبيقات التفاضل")
    app_type = st.selectbox("اختر التطبيق:", ["القيم العظمى والصغرى", "معدلات التغير المرتبطة", "المماس والعمودي"])
    
    if st.button("شرح التطبيق"):
        with st.spinner("جاري جلب الشرح..."):
            explanation = get_ai_explanation(f"Explain the concept of {app_type} in differential calculus with an example.")
            st.info(explanation)
