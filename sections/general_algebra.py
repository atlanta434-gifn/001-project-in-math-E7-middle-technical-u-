import streamlit as st
from utils import section_header, get_ai_explanation
import sympy as sp

def show():
    section_header("الجبر العام", "حل المعادلات والتبسيط الجبري")
    
    st.markdown("""
    <div class="rtl">
        أدخل المعادلة الجبرية التي ترغب في حلها أو تبسيطها.
    </div>
    """, unsafe_allow_html=True)
    
    equation = st.text_input("المعادلة (مثال: x^2 + 5x + 6 = 0):", "x^2 + 5x + 6 = 0")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("حل المعادلة"):
            with st.spinner("جاري الحل..."):
                # Symbolic solution attempt
                try:
                    eq_parts = equation.split('=')
                    if len(eq_parts) == 2:
                        lhs = sp.sympify(eq_parts[0])
                        rhs = sp.sympify(eq_parts[1])
                        sol = sp.solve(lhs - rhs)
                        st.success(f"الجذور: {sol}")
                except:
                    st.warning("تعذر الحل الرمزي المباشر، جاري استخدام الذكاء الاصطناعي...")
                
                explanation = get_ai_explanation(f"Solve the algebraic equation: {equation}. Provide step-by-step explanation.")
                st.markdown(explanation)
                
    with col2:
        if st.button("تبسيط التعبير"):
            with st.spinner("جاري التبسيط..."):
                explanation = get_ai_explanation(f"Simplify the algebraic expression: {equation}. Explain the steps.")
                st.markdown(explanation)
