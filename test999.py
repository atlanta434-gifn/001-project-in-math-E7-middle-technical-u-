import streamlit as st
import os
import numpy as np
import plotly.express as px
from openai import OpenAI

st.set_page_config(
    page_title="E7 Quantum Multiverse Hub",
    page_icon="♾️",
    layout="wide"
)

def build_clients():
    clients = []

    if os.getenv("OPENAI_API_KEY"):
        clients.append((
            "openai",
            OpenAI(api_key=os.getenv("OPENAI_API_KEY")),
            "gpt-4.1-mini"
        ))

    if os.getenv("GROQ_API_KEY"):
        clients.append((
            "groq",
            OpenAI(
                api_key=os.getenv("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1"
            ),
            "llama-3.1-70b-versatile"
        ))

    if os.getenv("DEEPSEEK_API_KEY"):
        clients.append((
            "deepseek",
            OpenAI(
                api_key=os.getenv("DEEPSEEK_API_KEY"),
                base_url="https://api.deepseek.com"
            ),
            "deepseek-chat"
        ))

    return clients

CLIENTS = build_clients()

def ask_ai(prompt, context="General Engineering"):
    if not CLIENTS:
        return "❌ لا توجد مفاتيح API مضافة في Secrets."

    full_prompt = f"""
أنت خبير أكاديمي عالمي.
اشرح بالتفصيل خطوة بخطوة وبأسلوب تعليمي واضح.

الموضوع:
{prompt}

السياق:
{context}
"""
    last_error = None

    for name, client, model in CLIENTS:
        try:
            r = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": full_prompt}],
                timeout=30
            )
            return r.choices[0].message.content
        except Exception as e:
            last_error = f"{name} failed: {e}"

    return f"❌ فشل جميع المحركات.\n{last_error}"

st.markdown("<h1 style='text-align:center;'>E7 QUANTUM MULTIVERSE HUB</h1>", unsafe_allow_html=True)

menu = st.selectbox(
    "اختر القسم:",
    ["المنطق الرقمي", "كيرشوف", "الدومين والرينج", "التفاضل", "الكم"]
)

if menu == "المنطق الرقمي":
    gates = st.multiselect("البوابات:", ["AND", "OR", "XOR"])
    inputs = st.text_input("المدخلات:", "1,1")
    if st.button("تحليل"):
        st.write(ask_ai(f"اشرح بوابات {gates} بمدخلات {inputs}"))

elif menu == "كيرشوف":
    desc = st.text_area("صف الدائرة:")
    if st.button("حل"):
        st.write(ask_ai(desc, "Circuit Analysis"))

elif menu == "الدومين والرينج":
    f = st.text_input("الدالة:", "sqrt(x-1)/(x-3)")
    x = np.linspace(-10, 10, 400)
    st.plotly_chart(px.line(x=x, y=np.sin(x)))
    if st.button("تحليل"):
        st.write(ask_ai(f"أوجد الدومين والرينج للدالة {f}"))

elif menu == "التفاضل":
    eq = st.text_input("المعادلة:", "x**3 - 2*x + 1")
    if st.button("حل"):
        st.write(ask_ai(f"حل تفاضلي وتكاملي للمعادلة {eq}"))

elif menu == "الكم":
    gate = st.selectbox("البوابة:", ["Hadamard", "CNOT", "Pauli-X"])
    if st.button("شرح"):
        st.write(ask_ai(f"اشرح بوابة {gate} الكمومية"))


