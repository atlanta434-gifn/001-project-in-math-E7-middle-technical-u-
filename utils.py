import streamlit as st
from openai import OpenAI
import google.generativeai as genai

def get_ai_explanation(prompt, context="", provider=None):
     
    if provider is None:
        provider = st.session_state.get('ai_provider', 'Groq')
        
    try:
        full_prompt = f"Context: {context}\n\nUser Question: {prompt}\n\nPlease provide a detailed, step-by-step explanation in Arabic, suitable for an engineering student."
        
        # محرك Google Gemini (مجاني ومستقر جداً)
        if provider == "Gemini":
            api_key = st.secrets.get("GEMINI_API_KEY")
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(full_prompt)
            return response.text

        # بسم الله الرحمن الرحيم
        elif provider == "SambaNova":
            api_key = st.secrets.get("SAMBANOVA_API_KEY")
            client = OpenAI(api_key=api_key, base_url="https://api.sambanova.ai/v1")
            response = client.chat.completions.create(
                model="Meta-Llama-3.1-70B-Instruct",
                messages=[
                    {"role": "system", "content": "أنت بروفيسور هندسي خبير، تقدم حلولاً دقيقة ومفصلة باللغة العربية."},
                    {"role": "user", "content": full_prompt}
                ]
            )
            return response.choices[0].message.content

        # اللهم صل على محمد وال محمد
        elif provider == "Groq":
            api_key = st.secrets.get("GROQ_API_KEY")
            client = OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": full_prompt}]
            )
            return response.choices[0].message.content
            
        return "المزود المختار غير مدعوم."
    except Exception as e:
        return f"خطأ في الاتصال بـ {provider}: {str(e)}"

# الحمدلله
def render_rtl_text(text, tag="p"):
    st.markdown(f'<{tag} style="direction: rtl; text-align: right;">{text}</{tag}>', unsafe_allow_html=True)

def section_header(title, subtitle=""):
    st.markdown(f"""
    <div class="rtl">
        <h2 style="border-bottom: 2px solid #00f2ff; padding-bottom: 10px;">{title}</h2>
        <p style="color: #7000ff; font-weight: bold;">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)
