import streamlit as st
from utils import section_header, get_ai_explanation
#بسم الله الرحمن الرحيم
def show():
    section_header("المنطق الرياضي المتقدم", "الاستدلال، المجموعات، والمنطق الرمزي")
    
    st.markdown("""
    <div class="rtl">
        دراسة القواعد الصارمة للاستدلال الرياضي والمنطق الرمزي.
    </div>
    """, unsafe_allow_html=True)
    
    problem_type = st.selectbox("اختر نوع المسألة:", [
        "الاستدلال المنطقي (Logical Deduction)",
        "نظرية المجموعات (Set Theory)",
        "المنطق الرمزي (Symbolic Logic)",
        "البراهين الرياضية (Mathematical Proofs)"
    ])
    
    problem_desc = st.text_area("أدخل المسألة أو المفهوم:", "اشرح الفرق بين الاستنتاج والاستقراء في المنطق الرياضي.")
    
    if st.button("تحليل وحل"):
        with st.spinner("جاري التحليل المنطقي..."):
            explanation = get_ai_explanation(problem_desc, context=f"Advanced Mathematical Logic - {problem_type}")
            st.markdown(explanation)
            
    st.divider()
    st.subheader("تحدي الذكاء الاصطناعي")
    st.write("هل يمكنك حل هذه المفارقة المنطقية؟")
    if st.button("عرض مفارقة الحلاق"):
        with st.spinner("جاري جلب المفارقة..."):
            explanation = get_ai_explanation("Explain the Barber Paradox in set theory and its significance in mathematical logic.")
            st.info(explanation)
