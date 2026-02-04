import streamlit as st
from utils import section_header, get_ai_explanation

def show():
    section_header("الإلكترونيات وأشباه الموصلات", "الديودات، الترانزستورات، والدوائر المتكاملة")
    
    st.markdown("""
    <div class="rtl">
        دراسة فيزياء أشباه الموصلات وكيفية عمل المكونات الإلكترونية الحديثة.
    </div>
    """, unsafe_allow_html=True)
    
    component = st.selectbox("اختر مكوناً إلكترونياً:", ["PN Junction Diode", "Bipolar Junction Transistor (BJT)", "MOSFET", "Zener Diode", "LED"])
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Diode_symbol.svg/200px-Diode_symbol.svg.png", caption="رمز المكون (مثال)")
        
    with col2:
        if st.button(f"شرح عمل {component}"):
            with st.spinner("جاري التحليل..."):
                explanation = get_ai_explanation(f"Explain the physics and operation of {component}. Include its V-I characteristics and common applications.")
                st.info(explanation)
                
    st.divider()
    st.subheader("فيزياء أشباه الموصلات")
    topic = st.selectbox("اختر موضوعاً:", ["Energy Bands", "P-type vs N-type", "Carrier Transport", "Fermi Level"])
    
    if st.button("شرح الموضوع"):
        with st.spinner("جاري جلب البيانات..."):
            explanation = get_ai_explanation(f"Explain the concept of {topic} in semiconductor physics.")
            st.markdown(explanation)
