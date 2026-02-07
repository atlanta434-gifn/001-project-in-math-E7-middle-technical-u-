import streamlit as st
import google.generativeai as genai
from openai import OpenAI

def get_ai_explanation(prompt, context="", provider=None):
    if provider is None:
        provider = st.session_state.get('ai_provider', 'Gemini')
        
    try:
        full_prompt = f"Context: {context}\n\nUser Question: {prompt}\n\nPlease provide a detailed explanation in Arabic."
        
        # 1. تصحيح محرك Gemini (استخدام الموديل المستقر)
        if provider == "Gemini":
            api_key = st.secrets.get("GEMINI_API_KEY")
            genai.configure(api_key=api_key)
            # استخدام gemini-1.5-flash بدون بادئة v1beta
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(full_prompt)
            return response.text

        # 2. تصحيح محرك SambaNova (تحديث اسم الموديل للمتاح حالياً)
        elif provider == "SambaNova":
            api_key = st.secrets.get("SAMBANOVA_API_KEY")
            client = OpenAI(api_key=api_key, base_url="https://api.sambanova.ai/v1")
            # تغيير الموديل إلى الإصدار الأكثر استقراراً لديهم
            response = client.chat.completions.create(
                model="Meta-Llama-3.1-405B-Instruct-v1", # أو "Meta-Llama-3.1-8B-Instruct" للتجربة
                messages=[{"role": "user", "content": full_prompt}]
            )
            return response.choices[0].message.content

        # 3. محرك Groq (الأضمن دائماً)
        elif provider == "Groq":
            api_key = st.secrets.get("GROQ_API_KEY")
            client = OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": full_prompt}]
            )
            return response.choices[0].message.content
            
        return "المزود غير مدعوم."
    except Exception as e:
        return f"خطأ في الاتصال بـ {provider}: {str(e)}"

# الدوال الأساسية لضمان عمل الأقسام الـ 18
def section_header(title, subtitle=""):
    st.markdown(f'<div class="rtl"><h2>{title}</h2><p style="color:#7000ff;">{subtitle}</p></div>', unsafe_allow_html=True)

def render_rtl_text(text, tag="p"):
    st.markdown(f'<{tag} style="direction:rtl;text-align:right;">{text}</{tag}>', unsafe_allow_html=True)
