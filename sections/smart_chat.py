import streamlit as st
# استدعاء الدالة الأساسية فقط لضمان عدم حدوث خطأ في حال نقص الدوال الأخرى
from utils import get_ai_explanation

def show():
    # تصميم واجهة الشات
    st.markdown("""
        <div style="text-align: center; padding: 20px; background: rgba(0, 242, 255, 0.1); border-radius: 15px; border: 1px solid #00f2ff; margin-bottom: 25px;">
            <h1 style="color: #00f2ff; margin: 0;">🧠 مساعد الذكاء الاصطناعي الهندسي</h1>
            <p style="color: #ffffff; font-size: 1.1em; margin-top: 10px;">نظام معالجة فوري مدعوم بـ 4 مفاتيح API</p>
        </div>
    """, unsafe_allow_html=True)

    # اختيار الموديل
    model_choice = st.selectbox(
        "اختر محرك التحليل:",
        ["llama-3.3-70b-versatile", "llama-3.1-70b-versatile", "mixtral-8x7b-32768"],
        index=0
    )

    # تهيئة سجل المحادثة
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # عرض الرسائل بتنسيق محاذراة اليمين (RTL) يدوي لضمان العمل
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(f'<div style="direction: rtl; text-align: right;">{message["content"]}</div>', unsafe_allow_html=True)

    # استقبال مدخلات المستخدم
    if prompt := st.chat_input("اسأل عن أي مفهوم هندسي..."):
        # إضافة رسالة المستخدم
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(f'<div style="direction: rtl; text-align: right;">{prompt}</div>', unsafe_allow_html=True)

        # جلب الرد من مساعد الذكاء الاصطناعي
        with st.chat_message("assistant"):
            with st.spinner("جاري التحليل عبر Groq..."):
                try:
                    # نمرر اسم الموديل المختار مباشرة كـ provider
                    response = get_ai_explanation(prompt, context="Engineering Smart Chat", provider=model_choice)
                    st.markdown(f'<div style="direction: rtl; text-align: right;">{response}</div>', unsafe_allow_html=True)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"حدث خطأ في الاتصال: {str(e)}")

    # زر مسح الذاكرة
    if st.sidebar.button("🗑️ مسح محادثة الشات"):
        st.session_state.messages = []
        st.rerun()
