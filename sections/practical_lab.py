import streamlit as st
from utils import section_header, get_ai_explanation

def show():
    section_header("المختبر العملي DC-AC", "تجارب تفاعلية وإرشادات مخبرية")
    
    st.markdown("""
    <div class="rtl">
        هذا القسم يحاكي التجارب العملية التي يتم إجراؤها في مختبرات الكهرباء والإلكترونيك.
    </div>
    """, unsafe_allow_html=True)
    
    experiment = st.selectbox("اختر تجربة:", [
        "تحقيق قانون أوم (Ohm's Law)",
        "ربط المقاومات على التوالي والتوازي",
        "شحن وتفريغ المتسعة (RC Circuit)",
        "خصائص الديود (Diode Characteristics)",
        "استخدام الأوسيلوسكوب (Oscilloscope)"
    ])
    
    st.subheader(f"خطوات تجربة: {experiment}")
    
    if st.button("عرض دليل التجربة"):
        with st.spinner("جاري إعداد الدليل..."):
            explanation = get_ai_explanation(f"Provide a detailed lab manual for the experiment: {experiment}. Include objectives, equipment, procedure, and expected results.")
            st.markdown(explanation)
            
    st.divider()
    st.subheader("محاكي القياس")
    col1, col2, col3 = st.columns(3)
    with col1: v = st.number_input("الجهد المقاس (V):", value=5.0)
    with col2: r = st.number_input("المقاومة (Ω):", value=100.0)
    with col3: 
        i = v / r if r != 0 else 0
        st.metric("التيار المحسوب (I)", f"{i:.4f} A")
        
    st.info("نصيحة مخبرية: تأكد دائماً من فصل الطاقة قبل تغيير التوصيلات في الدائرة.")
