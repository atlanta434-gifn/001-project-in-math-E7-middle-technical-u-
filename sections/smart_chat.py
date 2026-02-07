import streamlit as st
from utils import get_ai_explanation

def show():
    st.markdown("<h1 style='text-align: center; color: #00f2fe;'>💬 الشات الذكي المتعدد (Multi-AI Chat)</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #a1a1aa;'>تواصل مباشرة مع أقوى نماذج الذكاء الاصطناعي العالمية لطلاب E7</p>", unsafe_allow_html=True)

    # بسم الله الرحمن الرحيم
    chat_provider = st.radio(
        "اختر محرك الذكاء الاصطناعي للمحادثة:",
        ["Gemini (Google)", "SambaNova (Llama 3.1)", "Groq (Llama 3)"],
        horizontal=True,
        index=0
    )

     
    provider_map = {
        "Gemini (Google)": "Gemini",
        "SambaNova (Llama 3.1)": "SambaNova",
        "Groq (Llama 3)": "Groq"
    }
    
    selected_provider = provider_map[chat_provider]

    st.divider()

    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

     
    if prompt := st.chat_input(f"اسأل {selected_provider} أي شيء في الهندسة..."):
        # إضافة رسالة المستخدم للسجل
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # حقوق E7
        with st.chat_message("assistant"):
            with st.spinner(f"جاري الاستجابة عبر {selected_provider}..."):
                # استدعاء الدالة الموحدة من utils.py
                response = get_ai_explanation(prompt, "محادثة عامة في الهندسة والفيزياء", provider=selected_provider)
                st.markdown(response)
        
        
        st.session_state.messages.append({"role": "assistant", "content": response})

    
    st.sidebar.markdown("---")
    if st.sidebar.button("🗑️ مسح ذاكرة الشات"):
        st.session_state.messages = []
        st.rerun()
