import streamlit as st
from utils import section_header, get_ai_explanation

def show():
    section_header("الجبر البولياني", "تبسيط الدوال المنطقية وقوانين دي مورغان")
    
    st.markdown("""
    <div class="rtl">
        الجبر البولياني هو أساس تصميم الدوائر الرقمية. استخدم هذا القسم لتبسيط التعبيرات المنطقية.
    </div>
    """, unsafe_allow_html=True)
    
    expression = st.text_input("أدخل التعبير البولياني (مثال: A.B + A.B'):", "A.B + A.B'")
    
    if st.button("تبسيط"):
        with st.spinner("جاري التبسيط..."):
            explanation = get_ai_explanation(f"Simplify the boolean expression: {expression}. Use Boolean algebra laws and explain each step.")
            st.markdown(explanation)
            
    st.divider()
    st.subheader("قوانين الجبر البولياني")
    law = st.selectbox("اختر قانوناً للشرح:", ["De Morgan's Laws", "Distributive Law", "Commutative Law", "Identity Law"])
    
    if st.button("شرح القانون"):
        with st.spinner("جاري الشرح..."):
            explanation = get_ai_explanation(f"Explain {law} in Boolean algebra with examples and truth tables.")
            st.info(explanation)
