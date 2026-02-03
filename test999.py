import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import sympy as sp
from groq import Groq
import openai
from datetime import datetime

# بسم الله الرحمن الرحيم
st.set_page_config(page_title="E7 Quantum Multiverse Hub", layout="wide", page_icon="♾️")

# اللهم صل على محمد وال محمد
API_KEYS = {
    "OPENAI": "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",
    "DEEPSEEK": "sk-3954bc2eabef472e990e8852da62ca1b",
    "GROQ": "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",
    "COMET": "sk-8qYRpTvLRkYEDV7zHvsmjkAje1nqwtwZUhpggRXpUyJXDM9J",
    "OPENQUANTUM": "s_34337906708641699009dd703cb403d5"
}

def ask_ai(prompt, context="General Engineering"):
    
    engines = [
        ("OpenAI GPT-4o", "gpt-4o", "openai"),
        ("DeepSeek", "deepseek-chat", "deepseek"),
        ("Groq Llama", "llama-3.3-70b-versatile", "groq")
    ]
    
    for name, model_id, provider in engines:
        try:
            if provider == "openai":
                client = openai.OpenAI(api_key=API_KEYS["OPENAI"])
                res = client.chat.completions.create(model=model_id, messages=[{"role": "user", "content": prompt}])
            elif provider == "deepseek":
                client = openai.OpenAI(api_key=API_KEYS["DEEPSEEK"], base_url="https://api.deepseek.com")
                res = client.chat.completions.create(model=model_id, messages=[{"role": "user", "content": prompt}])
            elif provider == "groq":
                client = Groq(api_key=API_KEYS["GROQ"])
                res = client.chat.completions.create(model=model_id, messages=[{"role": "user", "content": prompt}])
            
            return res.choices[0].message.content + f"\n\n*(تمت المعالجة بواسطة: {name})*"
        except Exception as e:
            print(f"Error in {name}: {e}") # سيظهر الخطأ في التيرمينال فقط لتعرف السبب
            continue # جرب المحرك التالي
            
    return "⚠️ جميع المحركات مشغولة حالياً، يرجى إعادة المحاولة بعد 10 ثوانٍ."

# علي كاعد تفتر هنا مو
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle, #000814 0%, #001d3d 100%); color: #ffc300; }
    .quantum-card {
        background: rgba(0, 29, 61, 0.7);
        border: 1px solid #003566;
        padding: 25px; border-radius: 20px;
        box-shadow: 0 0 25px #003566;
        margin-bottom: 20px;
    }
    .main-title {
        font-family: 'Orbitron', sans-serif;
        background: linear-gradient(90deg, #ffc300, #00d4ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center; font-size: 3.5em; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# والله تعبت
st.markdown("<h1 class='main-title'>E7 QUANTUM MULTIVERSE HUB</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00d4ff;'> - جامعة التقنية الوسطى</p>", unsafe_allow_html=True)

# والله باردة
with st.sidebar:
    st.title("🌐 الملاحة الكونية")
    menu = st.selectbox("اختر البُعد الهندسي:", [
        "1. المنطق الرقمي والكمي", "2. الكيمياء والكهرباء", "3. كيرشوف والدوائر AC/DC", 
        "4. الرياضيات الجبرية", "5. الدومين والرينج الاحترافي", "6. التفاضل وتطبيقاته", 
        "7. التكامل وتطبيقاته", "8. الجبر البولياني", "9. المنطق الرياضي المكثف",
        "10. الحوسبة الكمومية", "11. فيزياء أشباه الموصلات", "12. مختبر DC/AC العملي", 
        "13. أساسيات الفيزياء والرياضيات", "14. فلسفة الرياضيات", "15. الرسم الهندسي (AutoCAD)",
        "16. أساسيات الكوانتم والفوتونات", "17. اللغة الإنجليزية الهندسية", "18. الفيزياء الكمومية"
    ])

# 7:38
if menu == "1. المنطق الرقمي والكمي":
    st.header("🔢 المنطق الرقمي والأنظمة الكمومية")
    col1, col2 = st.columns(2)
    with col1:
        gate_type = st.multiselect("ربط البوابات:", ["AND", "OR", "NAND", "NOR", "XOR", "NOT"])
        input_bits = st.text_input("المدخلات (مثال: 1,0):", "1,1")
    
    with col2:
        conversion_type = st.selectbox("التحويل بين الأنظمة:", ["Decimal to Binary", "Binary to Hex", "Quantum Qubit State"])
    
    if st.button("تحليل الدالة المنطقية"):
        res = ask_ai(f"اشرح بوابات {gate_type} بمدخلات {input_bits}. استخرج SOP و POS وجدول الحقيقة وارسم الدائرة منطقياً.")
        st.markdown(f"<div class='quantum-card'>{res}</div>", unsafe_allow_html=True)
        st.markdown("")

# كون نحصل الدرحات على هذا التعب :(
elif menu == "2. الكيمياء والكهرباء":
    st.header("🧪 الكيمياء الكهربائية والعناصر")
    element = st.text_input("أدخل العنصر أو المادة الكيميائية:", "Copper")
    if st.button("تحليل الخواص"):
        res = ask_ai(f"حلل مادة {element} كيميائياً وكهربائياً. اذكر الناقلية، التفاعلات، والاستخدامات في هندسة الكهرباء.")
        st.write(res)
        st.markdown("")

# باقيييي شوووية
elif menu == "3. كيرشوف والدوائر AC/DC":
    st.header("🔌 تحليل كيرشوف والربط المختلط")
    circuit_type = st.radio("نوع التيار:", ["DC", "AC (Phasor Analysis)"])
    problem_desc = st.text_area("صف الدائرة بالتفصيل:")
    if st.button("حل الدائرة"):
        res = ask_ai(f"حل المسألة التالية باستخدام KVL و KCL للتيار {circuit_type}: {problem_desc}. ارسم مسارات التيار ذهنياً.")
        st.write(res)
        st.markdown("")


elif menu == "5. الدومين والرينج الاحترافي":
    st.header("📉 تحليل الدومين والرينج المتقدم")
    func_str = st.text_input("أدخل الدالة y =", "sqrt(x-1)/(x-3)")
    
    
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        # الرسم التقليدي
        x = np.linspace(-10, 10, 400)
        y = np.sin(x) # مثال مبسط
        fig1 = px.line(x=x, y=y, title="Linear Plot")
        st.plotly_chart(fig1)
    with col_g2:
        # الرسم القطبي
        fig2 = px.scatter_polar(r=[1, 2, 3, 4], theta=[0, 45, 90, 135], title="Polar Plot")
        st.plotly_chart(fig2)
        
    if st.button("تحليل رياضي عميق"):
        st.write(ask_ai(f"أوجد الدومين والرينج للدالة {func_str} واشرح الفترات والخطوط التقاربية."))


elif menu in ["6. التفاضل وتطبيقاته", "7. التكامل وتطبيقاته"]:
    st.header(f"🧮 {menu}")
    topic = st.selectbox("اختر التطبيق:", ["Area under curve", "Volume of revolution", "Rate of change", "Optimization"])
    eq_math = st.text_input("المعادلة:", "x**3 - 2*x + 1")
    if st.button("بدء الحل التفصيلي"):
        st.write(ask_ai(f"حل {eq_math} ضمن تطبيق {topic} مع شرح كل خطوة والقوانين المستخدمة من ملفات Calculus الخاصة بنا."))
        st.markdown("")


elif menu == "10. الحوسبة الكمومية":
    st.header("🌌 Quantum Computing Frontier")
    q_gate = st.selectbox("البوابة الكمومية:", ["Hadamard (H)", "CNOT", "Pauli-X"])
    if st.button("محاكاة البوابة"):
        st.write(ask_ai(f"اشرح عمل بوابة {q_gate} وكيف تغير حالة الـ Qubit من 0 إلى Superposition."))
        st.markdown("[attachment_0](attachment)")


elif menu == "15. الرسم الهندسي (AutoCAD)":
    st.header("📐 تعليم الرسم الهندسي و AutoCAD")
    tool = st.selectbox("الأداة:", ["Line/Circle", "Layers", "3D Modeling", "Isometric View"])
    if st.button("شرح الأداة"):
        st.write(ask_ai(f"اشرح كيفية استخدام {tool} في AutoCAD 2024 للمهندسين المبتدئين خطوة بخطوة."))


elif menu == "17. اللغة الإنجليزية الهندسية":
    st.header("🇬🇧 English for Engineers")
    term = st.text_input("أدخل مصطلحاً هندسياً للتعلم:")
    if st.button("تعلم بطريقة مبتكرة"):
        st.write(ask_ai(f"اشرح المصطلح {term} بالإنجليزية والعربية، ضعه في جملة هندسية، واذكر كيف يلفظ بطريقة صحيحة."))

# الله اكبر ولله الحمد
st.markdown("---")
st.markdown("<p style='text-align:center;'>تم التطوير بواسطة المهم نحصل درجات شعبة E7 -</p>", unsafe_allow_html=True)


