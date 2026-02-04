import streamlit as st
from openai import OpenAI

def get_ai_explanation(prompt, context="General Engineering"):
    full_prompt = f"أنت بروفيسور هندسي من شعبة E7. اشرح بالتفصيل: {prompt}. السياق: {context}"
    
    # --- المحاولة الأولى: OpenAI ---
    try:
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": full_prompt}]
        )
        return response.choices[0].message.content
    except Exception as e1:
        # --- المحاولة الثانية: Groq (سريع جداً) ---
        try:
            # نستخدم Groq عبر مكتبة OpenAI لأنه متوافق معها
            client_groq = OpenAI(
                api_key=st.secrets["GROQ_API_KEY"],
                base_url="https://api.groq.com/openai/v1"
            )
            response = client_groq.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": full_prompt}]
            )
            return response.choices[0].message.content
        except Exception as e2:
            # --- المحاولة الثالثة: DeepSeek ---
            try:
                client_ds = OpenAI(
                    api_key=st.secrets["DEEPSEEK_API_KEY"],
                    base_url="https://api.deepseek.com"
                )
                response = client_ds.chat.completions.create(
                    model="deepseek-chat",
                    messages=[{"role": "user", "content": full_prompt}]
                )
                return response.choices[0].message.content
            except Exception as e3:
                return f"⚠️ جميع المحركات منشغلة حالياً. خطأ OpenAI: {str(e1)}"

def section_header(title, subtitle=""):
    st.markdown(f"""
    <div style="direction: rtl; text-align: right;">
        <h2 style="color: #00f2ff; border-bottom: 2px solid #7000ff;">{title}</h2>
        <p style="color: #a0a0a0;">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

