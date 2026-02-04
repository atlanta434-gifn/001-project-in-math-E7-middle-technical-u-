import streamlit as st
from utils import section_header, get_ai_explanation

def show():
    section_header("فلسفة الرياضيات", "تأملات في طبيعة الأرقام والمنطق")
    
    st.markdown("""
    <div class="rtl">
        هل الرياضيات اختراع أم اكتشاف؟ استكشف الجوانب الفلسفية للعلوم الرياضية.
    </div>
    """, unsafe_allow_html=True)
    
    topic = st.selectbox("اختر موضوعاً للنقاش:", [
        "طبيعة الأعداد الحقيقية",
        "اللانهاية في الرياضيات",
        "العلاقة بين الرياضيات والواقع",
        "منطق غودل وعدم الاكتمال",
        "الرياضيات والجمال"
    ])
    
    if st.button("ابدأ النقاش الفلسفي"):
        with st.spinner("جاري التفكير بعمق..."):
            explanation = get_ai_explanation(f"Discuss the philosophy of mathematics regarding: {topic}. Provide different perspectives and historical context.")
            st.markdown(explanation)
            
    st.divider()
    st.subheader("أقوال مأثورة")
    st.info('"الرياضيات هي لغة الطبيعة" - غاليليو غاليلي')
    
    st.subheader("اسأل الفيلسوف الآلي")
    user_q = st.text_input("اطرح سؤالاً فلسفياً حول الرياضيات:")
    if user_q:
        if st.button("إجابة"):
            with st.spinner("جاري التحليل..."):
                ans = get_ai_explanation(user_q, context="Philosophy of Mathematics")
                st.write(ans)
