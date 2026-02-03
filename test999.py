import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import sympy as sp
from groq import Groq
from datetime import datetime

# اللهم صل على محمد وعلى ال محمد
st.set_page_config(page_title="E7 Universal Engineering Hub", layout="wide", page_icon="🌐")

# شعندك تفتر هنا
client = Groq(api_key="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")

def get_ai_response(prompt):
    try:
        completion = client.chat.completions.create(
            messages=[{"role": "system", "content": "أنت نظام ذكاء اصطناعي هندسي عالمي مخصص لشعبة E7. تقدم حلولاً دقيقة، شروحات رياضية مفصلة، وتطبيقات عملية باللغة العربية."},
                      {"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
        )
        return completion.choices[0].message.content
    except: return "⚠️ المحرك الذكي في حالة صيانة حالياً، يرجى المحاولة لاحقاً."

# :((
st.markdown("""
    <style>
    .main { background-color: #0b0e14; }
    .stApp { background: linear-gradient(135deg, #0b0e14 0%, #1a1f2c 100%); }
    .header-style {
        background: rgba(46, 125, 50, 0.1);
        padding: 40px; border-radius: 20px;
        border: 1px solid #2e7d32;
        text-align: center; margin-bottom: 40px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .footer { text-align: center; padding: 20px; color: #666; font-size: 0.8em; }
    .quantum-card {
        background: linear-gradient(45deg, #12100e, #2b4162);
        padding: 20px; border-radius: 15px; border-left: 5px solid #00d4ff;
    }
    </style>
    """, unsafe_allow_html=True)

# لا اله الا الله
st.markdown(f"""
    <div class="header-style">
        <h1 style="color:#4caf50; font-family: 'Segoe UI'; letter-spacing: 2px;">E7 UNIVERSAL ENGINEERING PLATFORM</h1>
        <h4 style="color:white; opacity:0.8;">الجامعة التقنية الوسطى - كلية البوليتكنك - قسم الكترونيك و الذكاء الاصطناعي</h4>
        <p style="color:#bbb;">اعداد: علي نهاد | رؤى نديم | حسن محمد | عبدالله فراس | علي منتظر | أيمن مصطفى | حسين صباح</p>
    </div>
    """, unsafe_allow_html=True)

# مادري احس علي نهاد كاعد يفتر هنا
with st.sidebar:
    st.markdown("### 🛠️ المختبرات العالمية")
    app_mode = st.radio("", 
        ["🏠 الشاشة الرئيسية", 
         "🧪 كيمياء العناصر والكهرباء", 
         "📐 الرياضيات الفائقة (Calculus)", 
         "🔢 المنطق الرقمي (POS/SOP)", 
         "🔌 مختبر كيرشوف المتقدم", 
         "🌌 الحوسبة الكمومية (Quantum)"])
    st.markdown("---")
    st.write(f"© {datetime.now().year} E7 Engineering Team")

# 
if app_mode == "🏠 الشاشة الرئيسية":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("مرحباً بك في موقع شعبة E7")
        st.write("بعده الموقع قيد التطوير:)")
        if st.button("بدء محادثة"):
            query = st.text_input("شتريد؟")
            if query: st.write(get_ai_response(query))
    with col2:
        st.info("💡 **نصيحة اليوم:** استخدم قسم الرياضيات لتحليل المشتقات المعقدة وتطبيقاتها في هندسة الإلكترونيك.")

# --- 2. كيمياء العناصر والكهرباء ---
elif app_mode == "🧪 كيمياء العناصر والكهرباء":
    st.header("🧪 عناصر الجدول الدوري وتطبيقات الكهرباء")
    
    # بيانات العناصر
    elements = {
        "النحاس (Cu)": {"وصف": "أفضل موصل تجاري للكهرباء.", "تطبيقات": "الأسلاك، المحركات."},
        "السيليكون (Si)": {"وصف": "شبه موصل أساسي في الترانزستور.", "تطبيقات": "الرقائق الذكية، الخلايا الشمسية."},
        "الفضة (Ag)": {"وصف": "أعلى ناقلية كهربائية معروفة.", "تطبيقات": "المفاتيح الحساسة، الألواح المتطورة."},
        "الجرمانيوم (Ge)": {"وصف": "شبه موصل يستخدم في الترددات العالية.", "تطبيقات": "أجهزة الكشف عن الإشعاع."}
    }
    
    c1, c2 = st.columns(2)
    el1 = c1.selectbox("اختر العنصر الأول:", list(elements.keys()))
    el2 = c2.selectbox("اختر العنصر الثاني للمقارنة:", list(elements.keys()))
    
    if st.button("مقارنة ذكية وتطبيقاتها في الكهرباء"):
        comparison_prompt = f"قارن بين {el1} و {el2} من حيث الخصائص الذرية، الناقلية الكهربائية، واشرح أين يستخدم كل منهما في صناعة الدوائر الإلكترونية والذكاء الاصطناعي."
        st.markdown(get_ai_response(comparison_prompt))

# --- 3. الرياضيات الفائقة ---
elif app_mode == "📐 الرياضيات الفائقة (Calculus)":
    st.header("📐 مختبر التحليل الرياضي (Domain, Range, Calculus)")
    
    formula_input = st.text_input("أدخل الدالة (مثال: x**3 + sin(x) + sqrt(x)):", "x**2")
    x_sym = sp.symbols('x')
    
    try:
        expr = sp.sympify(formula_input)
        derivative = sp.diff(expr, x_sym)
        integral = sp.integrate(expr, x_sym)
        
        st.latex(f"f(x) = {sp.latex(expr)}")
        col_res1, col_res2 = st.columns(2)
        col_res1.metric("المشتقة الأولى", str(derivative))
        col_res2.metric("التكامل غير المحدد", str(integral))
        
        # الرسم البياني فائق الدقة
        x_vals = np.linspace(-10, 10, 1000)
        f_lambdified = sp.lambdify(x_sym, expr, "numpy")
        y_vals = f_lambdified(x_vals)
        
        fig = go.Figure(go.Scatter(x=x_vals, y=y_vals, line=dict(color='#00ff88', width=2)))
        st.plotly_chart(fig.update_layout(template="plotly_dark", title="الرسم البياني التفصيلي"))
        
        if st.button("تحليل الدومين والرينج والتطبيقات الهندسية"):
            st.markdown(get_ai_response(f"حلل الدالة {formula_input} من حيث الدومين والرينج، واشرح أهمية مشتقتها وتكاملها في تطبيقات هندسية واقعية (مثل معالجة الإشارات أو أنظمة التحكم)."))
    except: st.error("⚠️ خطأ في الصيغة الرياضية. يرجى استخدام صيغة Python (مثل x**2).")

# --- 4. المنطق الرقمي (POS/SOP) ---
elif app_mode == "🔢 المنطق الرقمي (POS/SOP)":
    st.header("🔢 الأنظمة الرقمية المتقدمة")
    st.write("أدخل الـ Minterms لاستخراج معادلة SOP أو Maxterms لـ POS.")
    
    logic_type = st.radio("التمثيل:", ["SOP (Sum of Products)", "POS (Product of Sums)"])
    terms = st.text_input("أدخل الأرقام (مثال: 0, 1, 3, 7):", "1, 2, 4")
    
    if st.button("توليد جدول الحقيقة وتصميم البوابات"):
        st.markdown(get_ai_response(f"اشرح بالتفصيل كيفية بناء معادلة {logic_type} للمدخلات {terms}. ارسم جدول الحقيقة ذهنياً واشرح أنواع البوابات (AND, OR, NOT) المطلوبة للتنفيذ."))

# --- 5. مختبر كيرشوف ---
elif app_mode == "🔌 مختبر كيرشوف المتقدم":
    st.header("🔌 Kirchhoff's Laws Solver")
    st.write("حل شبكات الدوائر المعقدة باستخدام قوانين كيرشوف للجهد والتيار.")
    
    circuit_desc = st.text_area("صف الدائرة الكهربائية:", "بطارية 20 فولت، مقاومة R1=10 أوم على التوالي، ثم تفرع لمقاومتين R2=5 و R3=5 أوم.")
    
    if st.button("حل الدائرة ورسم مسارات التيار"):
        st.markdown(get_ai_response(f"بناءً على الوصف التالي: '{circuit_desc}'، استخدم قوانين كيرشوف لحساب التيارات في كل فرع والجهد على كل مقاومة واشرح الخطوات بالتفصيل."))

# --- 6. الحوسبة الكمومية ---
elif app_mode == "🌌 الحوسبة الكمومية (Quantum)":
    st.header("🌌 بوابة الحوسبة الكمومية")
    st.markdown("""<div class="quantum-card">مرحباً بك في عصر الـ Qubit. هنا لا نستخدم 0 و 1 فقط، بل نستخدم التراكب الكمي.</div>""", unsafe_allow_html=True)
    
    concept = st.selectbox("اختر المفهوم الكمي:", ["Superposition", "Entanglement", "Quantum Gates (Hadamard, CNOT)"])
    
    if st.button("شرح وتطبيق محاكاة"):
        st.markdown(get_ai_response(f"اشرح مفهوم {concept} في الحوسبة الكمومية، وكيف يختلف عن الحوسبة التقليدية، وما هي تطبيقاته في مستقبل الذكاء الاصطناعي."))

# --- الفوتر ---
st.markdown(f"""
    <div class="footer">
        <hr>
        شعبة E7 - احسن شعبة E7 - الجامعة التقنية الوسطى<br>
        تم التطوير ليكون المشروع الأفضل لعام {datetime.now().year}
    </div>
    """, unsafe_allow_html=True)

