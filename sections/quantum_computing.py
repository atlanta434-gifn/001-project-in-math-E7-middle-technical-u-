import streamlit as st
from utils import section_header, get_ai_explanation

def show():
    section_header("الحوسبة الكمية", "البوابات الكمية، الكيوبتات، والتشابك")
    
    st.markdown("""
    <div class="rtl">
        مرحباً بك في مستقبل الحوسبة. استكشف مفاهيم الكيوبتات والبوابات الكمية.
    </div>
    """, unsafe_allow_html=True)
    
    q_gate = st.selectbox("اختر بوابة كمية للمحاكاة والشرح:", ["Hadamard (H)", "Pauli-X (NOT)", "Pauli-Y", "Pauli-Z", "CNOT"])
    
    if st.button("محاكاة وشرح"):
        with st.spinner("جاري معالجة البيانات الكمية..."):
            explanation = get_ai_explanation(f"Explain the quantum gate {q_gate}. Describe its effect on a qubit state and show its matrix representation.")
            st.markdown(explanation)
            
    st.divider()
    st.subheader("مفاهيم متقدمة")
    concept = st.radio("اختر مفهوماً:", ["Superposition (التراكب)", "Entanglement (التشابك)", "Quantum Teleportation"], horizontal=True)
    
    if st.button("اشرح المفهوم"):
        with st.spinner("جاري جلب الشرح..."):
            explanation = get_ai_explanation(f"Explain the concept of {concept} in quantum computing for engineering students.")
            st.info(explanation)
            
    st.subheader("تحدي البرمجة الكمية")
    st.write("كيف يمكننا بناء دائرة كمية لإنشاء حالة Bell؟")
    if st.button("عرض الحل"):
        with st.spinner("جاري الحل..."):
            explanation = get_ai_explanation("How to create a Bell state using quantum gates (H and CNOT)? Provide the circuit steps and explanation.")
            st.success(explanation)
