import streamlit as st
from utils import get_ai_explanation

def show():
    st.markdown("<h1 style='text-align: center; color: #00f2fe;'>💬 الشات الذكي المتعدد (Multi-AI Chat)</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #a1a1aa;'>تواصل مباشرة مع أقوى نماذج الذكاء الاصطناعي العالمية</p>", unsafe_allow_html=True)

    # اختيار المحرك داخل القسم
    chat_provider = st.radio(
        "اختر محرك الذكاء الاصطناعي للمحادثة:",
        ["OpenAI (GPT-4o)", "DeepSeek (V3/R1)", "Groq (Llama 3)"],
        horizontal=True,
        index=0
    )

    # خريطة للمزودين
    provider_map = {
        "OpenAI (GPT-4o)": "OpenAI",
        "DeepSeek (V3/R1)": "DeepSeek",
        "Groq (Llama 3)": "Groq"
    }
    
    selected_provider = provider_map[chat_provider]

    st.divider()

    # تهيئة سجل المحادثة في session_state إذا لم يكن موجوداً
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # عرض الرسائل السابقة
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # مدخل الشات
    if prompt := st.chat_input(f"اسأل {selected_provider} أي شيء..."):
        # إضافة رسالة المستخدم للسجل
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # الحصول على رد الذكاء الاصطناعي
        with st.chat_message("assistant"):
            with st.spinner(f"جاري التفكير عبر {selected_provider}..."):
                # نستخدم الدالة الموجودة في utils مع تمرير المزود المختار
                # قمنا بتعديل utils سابقاً ليدعم تمرير المزود
                response = get_ai_explanation(prompt, "عام", provider=selected_provider)
                st.markdown(response)
        
        # إضافة رد المساعد للسجل
        st.session_state.messages.append({"role": "assistant", "content": response})

    # زر لمسح المحادثة
    if st.button("🗑️ مسح المحادثة"):
        st.session_state.messages = []
        st.rerun()
