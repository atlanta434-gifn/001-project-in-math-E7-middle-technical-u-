import streamlit as st
from utils import section_header, get_ai_explanation

def show():
    section_header("تحليل الدوائر (Kirchhoff)", "قوانين KVL و KCL وتحليل الدوائر المعقدة")
    
    st.markdown("""
    <div class="rtl">
        قم بإدخال تفاصيل الدائرة الكهربائية للحصول على تحليل كامل باستخدام قوانين كيرشوف.
    </div>
    """, unsafe_allow_html=True)
    
    circuit_type = st.radio("نوع الدائرة:", ["DC (تيار مستمر)", "AC (تيار متناوب)"], horizontal=True)
    
    with st.expander("إدخال بيانات الدائرة", expanded=True):
        voltage_source = st.number_input("مصدر الجهد (V):", value=12.0)
        resistors = st.text_input("قيم المقاومات (أوم، مفصولة بفاصلة):", "10, 20, 30")
        connection = st.selectbox("نوع الربط:", ["توالي (Series)", "توازي (Parallel)", "مختلط (Mixed)"])
        
    if st.button("تحليل الدائرة"):
        with st.spinner("جاري حساب النتائج..."):
            prompt = f"Analyze a {circuit_type} circuit with a {voltage_source}V source and resistors {resistors} connected in {connection}. Provide step-by-step solution using KVL/KCL."
            explanation = get_ai_explanation(prompt)
            st.markdown("### الحل التفصيلي:")
            st.markdown(explanation)
            
    st.divider()
    st.subheader("تمثيل بصري (مخطط توضيحي)")
    st.info("سيتم هنا عرض مخططات ديناميكية للدوائر في التحديثات القادمة.")
    
    # Example of AI-powered problem solver
    st.subheader("مساعد حل المسائل")
    problem_desc = st.text_area("اصف المسألة هنا:", "دائرة تحتوي على مصدرين جهد وثلاث مقاومات، جد التيار في الفرع الأوسط...")
    if st.button("حل المسألة"):
        with st.spinner("جاري الحل..."):
            solution = get_ai_explanation(problem_desc, context="Circuit Analysis, KVL, KCL")
            st.success(solution)
