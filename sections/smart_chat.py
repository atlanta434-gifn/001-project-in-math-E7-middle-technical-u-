import streamlit as st
from utils import get_ai_explanation, render_rtl_text

def show():
    # عنوان القسم بتنسيق عصري
    st.markdown("""
        <div style="text-align: center; padding: 20px; background: rgba(0, 242, 255, 0.1); border-radius: 15px; border: 1px solid #00f2ff; margin-bottom: 25px;">
            <h1 style="color: #00f2ff; margin: 0;">🧠 مساعد الذكاء الاصطناعي الهندسي</h1>
            <p style="color: #ffffff; font-size: 1.1em; margin-top: 10px;">مدعوم بتقنية Groq LPU لسرعة استجابة فائقة</p>
        </div>
    """, unsafe_allow_html=True)

    # نظام اختيار النموذج
    col1, col2 = st.columns([1, 1])
    with col1:
        model_choice = st.selectbox(
            "اختر محرك التحليل:",
            ["Llama 3.3 (الأقوى هندسياً)", "Llama 3.1 (الاستجابة السريعة)", "Mixtral (للمنطق والبرمجة)"],
            help="نحن نستخدم 4 مفاتيح API لضمان عدم توقف الخدمة."
        )
    
    with col2:
        st.info("💡 الموقع يعمل الآن بنظام توزيع الحمل لضمان الاستقرار.")

    # خريطة النماذج
    model_map = {
        "Llama 3.3 (الأقوى هندسياً)": "llama-3.3-70b-versatile",
        "Llama 3.1 (الاستجابة السريعة)": "llama-3.1-70b-versatile",
        "Mixtral (للمنطق والبرمجة)": "mixtral-8x7b-32768"
    }

    # واجهة الشات - تأكد من تهيئة الحالة
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # عرض الرسائل السابقة
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            render_rtl_text(message["content"])

    # مدخل الشات
    if prompt := st.chat_input("اسأل عن أي مفهوم هندسي أو تقني..."):
        # 1. إضافة رسالة المستخدم للحالة وعرضها
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            render_rtl_text(prompt)

        # 2. جلب رد الذكاء الاصطناعي
        with st.chat_message("assistant"):
            with st.spinner("جاري التفكير والتحليل..."):
                response = get_ai_explanation(
                    prompt, 
                    context=f"Engineering Chat Mode - Model: {model_choice}",
                    provider=model_map[model_choice]
                )
                render_rtl_text(response)
                # 3. الحفظ في الحالة (هذا السطر كان مفقوداً)
                st.session_state.messages.append({"role": "assistant", "content": response})
