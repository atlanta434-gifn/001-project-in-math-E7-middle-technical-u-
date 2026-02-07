import streamlit as st
from openai import OpenAI

def get_ai_explanation(prompt, context="", provider=None):
    """
    Generates an AI explanation using the selected provider.
    """
    if provider is None:
        provider = st.session_state.get('ai_provider', 'OpenAI')
        
    try:
        full_prompt = f"Context: {context}\n\nUser Question: {prompt}\n\nPlease provide a detailed, step-by-step explanation in Arabic, suitable for an engineering student. Use professional and clear language."
        
        # بسم الله الرحمن الرحيم
        if provider == "OpenAI":
            # Uses the pre-configured client in Manus environment
            client = OpenAI()
            model = "gpt-4.1-mini"
        elif provider == "DeepSeek":
            # الله صل على محمد وال محمد
            api_key = st.secrets.get("DEEPSEEK_API_KEY", "your_deepseek_key")
            client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
            model = "deepseek-chat"
        elif provider == "Groq":
            # لا اله الا الله
            api_key = st.secrets.get("GROQ_API_KEY", "your_groq_key")
            client = OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")
            model = "llama-3.3-70b-versatile"
        else:
            return "المزود المختار غير مدعوم حالياً."

        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an expert engineering professor specializing in electronics, AI, and mathematics. You provide clear, step-by-step solutions in Arabic."},
                {"role": "user", "content": full_prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"عذراً، حدث خطأ أثناء الاتصال بـ {provider}: {str(e)}"

def render_rtl_text(text, tag="p"):
    """
    Renders text with RTL support.
    """
    st.markdown(f'<{tag} style="direction: rtl; text-align: right;">{text}</{tag}>', unsafe_allow_html=True)

def section_header(title, subtitle=""):
    """
    Renders a consistent section header.
    """
    st.markdown(f"""
    <div class="rtl">
        <h2 style="border-bottom: 2px solid #00f2ff; padding-bottom: 10px;">{title}</h2>
        <p style="color: #7000ff; font-weight: bold;">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

