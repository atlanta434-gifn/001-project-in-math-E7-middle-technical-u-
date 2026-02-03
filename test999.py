import streamlit as st
import numpy as np
import plotly.graph_objects as go
import sympy as sp
from groq import Groq
import openai
from datetime import datetime

# --- إعدادات الحماية والواجهة ---
st.set_page_config(page_title="E7 Quantum Universe", layout="wide")

# جلب المفاتيح بأمان
keys = st.secrets

# تعريف العملاء
client_oa = openai.OpenAI(api_key=keys["OPENAI_KEY"])
client_ds = openai.OpenAI(api_key=keys["DEEPSEEK_KEY"], base_url="https://api.deepseek.com")
client_gr = Groq(api_key=keys["GROQ_KEY"])

def ask_ai(prompt, section_name):
    """محرك الاستجابة الشامل خطوة بخطوة"""
    full_prompt = f"أنت بروفيسور هندسي عالمي. في قسم {section_name}، حل المسألة التالية بالتفصيل الممل، مع شرح القوانين والأساسيات والخطوات الصغيرة جداً: {prompt}"
    try:
        # المحاولة بـ GPT-4o كخيار أول للدقة
        res = client_oa.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": full_prompt}])
        return res.choices[0].message.content
    except:
        try: # التبديل لـ Groq للسرعة
            res = client_gr.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role": "user", "content": full_prompt}])
            return res.choices[0].message.content
        except:
            return "⚠️ عذراً، المحركات الهندسية قيد التحديث حالياً."

# --- التنسيق البصري العالمي ---
st.markdown("""
    <style>
    .stApp { background: #010409; color: #e6edf3; }
    .main-header { background: linear-gradient(90deg, #1f6feb, #238636); padding: 30px; border-radius: 15px; text-align: center; border: 1px solid #30363d; }
    .section-card { background: #0d1117; border: 1px solid #30363d; padding: 20px; border-radius: 10px; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# الهيدر مع الأسماء
st.markdown(f"""
    <div class="main-header">
        <h1 style="color:white; margin:0;">E7 QUANTUM MULTIVERSE HUB</h1>
        <p style="color:#8b949e;">:</p>
        <p style="color:#58a6ff; font-weight:bold;">علي نهاد | رؤى نديم | حسن محمد | عبدالله فراس | علي منتظر | أيمن مصطفى | حسين صباح</p>
    </div>
    """, unsafe_allow_html=True)

# --- القائمة الجانبية (19 قسماً) ---
with st.sidebar:
    st.title("🌐 الأقسام التخصصية")
    menu = st.radio("اختر القسم المطلوب:", [
        "1. المنطق الرقمي وبوابات SOP/POS", "2. الكيمياء الكهربائية والعناصر", "3. كيرشوف والربط المختلط AC/DC",
        "4. الرياضيات العامة الجبرية", "5. الدومين والرينج الاحترافي", "6. التفاضل وتطبيقاته",
        "7. التكامل وتطبيقاته", "8. الجبر البولياني", "9. المنطق الرياضي المكثف",
        "10. الحوسبة الكمومية (Quantum)", "11. فيزياء أشباه الموصلات", "12. مختبر DC-AC العملي",
        "13. أساسيات الرياضيات والفيزياء", "14. فلسفة الرياضيات", "15. الرسم الهندسي (AutoCAD)",
        "16. أساسيات الكوانتم والفوتونات", "17. اللغة الإنجليزية للعرب", "18. الفيزياء الكمومية وأهميتها"
    ])

# --- تشغيل الأقسام ---
st.write(f"### {menu}")

# 1. المنطق الرقمي
if menu == "1. المنطق الرقمي وبوابات SOP/POS":
    col1, col2 = st.columns(2)
    with col1:
        logic_in = st.text_area("أدخل التعبير المنطقي أو المينتيرمز:", "F(A,B,C) = Σm(0,2,4,6)")
        gate = st.selectbox("اختر البوابة الأساسية للتصميم:", ["AND", "NAND", "OR", "XOR"])
    with col2:
        st.info("سيقوم الذكاء الاصطناعي برسم Truth Table واستخراج SOP/POS.")
    if st.button("تحليل وتصميم"):
        st.markdown(ask_ai(f"حلل {logic_in} باستخدام بوابات {gate} وحولها بين الأنظمة الرقمية والكمومية.", menu))
        

# 2. الكيمياء والكهرباء
elif menu == "2. الكيمياء الكهربائية والعناصر":
    element = st.text_input("أدخل العنصر أو المادة الكيميائية لمقارنتها:", "Silicon vs Germanium")
    if st.button("تحليل الخواص الكيميائية"):
        st.markdown(ask_ai(f"قارن بين المواد التالية من حيث الخواص الكيميائية والكهربائية والاستخدامات: {element}", menu))

# 3. كيرشوف والربط المختلط
elif menu == "3. كيرشوف والربط المختلط AC/DC":
    prob = st.text_area("أدخل تفاصيل الدائرة (مقاومات، فولتية، تردد):")
    if st.button("بدء التحليل الشبكي"):
        st.markdown(ask_ai(f"حل الدائرة التالية باستخدام قوانين كيرشوف مع رسم الدالة وتوضيح فرق الطور في AC: {prob}", menu))
        

# 5. الدومين والرينج
elif menu == "5. الدومين والرينج الاحترافي":
    eq = st.text_input("أدخل المعادلة:", "y = sqrt(x**2 - 9)")
    if st.button("تحليل النطاق والمدى"):
        st.markdown(ask_ai(f"أوجد Domain و Range لـ {eq} واشرحها بـ 4 أنواع من الرسم البياني.", menu))
        # رسم بياني تفاعلي
        x = np.linspace(-10, 10, 400)
        fig = go.Figure(data=go.Scatter(x=x, y=np.sin(x), name="Domain Plot")) # مثال للرسم
        st.plotly_chart(fig)

# 6 & 7. التفاضل والتكامل
elif menu in ["6. التفاضل وتطبيقاته", "7. التكامل وتطبيقاته"]:
    task = st.text_input("أدخل المعادلة المراد معالجتها:")
    if st.button("حل تفصيلي مع التطبيقات"):
        st.markdown(ask_ai(f"حل {task} واذكر جميع تطبيقاتها الهندسية خطوة بخطوة.", menu))
        

# 10. الحوسبة الكمومية
elif menu == "10. الحوسبة الكمومية (Quantum)":
    topic = st.selectbox("الموضوع:", ["Qubits", "Entanglement", "Superposition"])
    if st.button("شرح كمومي عميق"):
        st.markdown(ask_ai(f"اشرح {topic} بطريقة الحوسبة الكمومية المعقدة والبسيطة.", menu))

# 15. الرسم الهندسي
elif menu == "15. الرسم الهندسي (AutoCAD)":
    cmd = st.text_input("ماذا تريد أن تتعلم في الأوتوكاد؟", "رسم المساقط الثلاثة")
    if st.button("عرض خطوات الرسم"):
        st.markdown(ask_ai(f"اشرح كيفية تنفيذ {cmd} في AutoCAD مع الأوامر المختصرة.", menu))

# 17. اللغة الإنجليزية
elif menu == "17. اللغة الإنجليزية للعرب":
    text = st.text_input("أدخل الجملة أو المصطلح الهندسي:")
    if st.button("ترجمة وتعليم مبتكر"):
        st.markdown(ask_ai(f"ترجم ووضح النطق والقواعد الهندسية لـ: {text}", menu))

# (بقية الأقسام تعمل بنفس الطريقة عبر استدعاء ask_ai)
else:
    st.info("هذا القسم قيد التفعيل عبر محرك الذكاء الاصطناعي... أدخل سؤالك أدناه.")
    user_q = st.text_area("أدخل استفسارك هنا:")
    if st.button("تحليل"):
        st.markdown(ask_ai(user_q, menu))

st.markdown("---")
st.write(f"التاريخ: {datetime.now().strftime('%Y-%m-%d')} | ")


