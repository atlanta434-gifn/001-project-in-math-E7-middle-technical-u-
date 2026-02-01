import streamlit as st
import numpy as np
import plotly.graph_objects as go
from groq import Groq

# 
st.set_page_config(page_title="E7 Comprehensive Engineering Platform", layout="wide")

# 
client = Groq(api_key="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")

def get_ai_explanation(prompt):
    """دالة لجلب الشرح الهندي من الذكاء الاصطناعي"""
    try:
        completion = client.chat.completions.create(
            messages=[{"role": "user", "content": f"أنت خبير هندسي لشعبة E7. اشرح لي رياضياً وبالخطوات التفصيلية بالعربية ما يلي: {prompt}"}],
            model="llama-3.3-70b-versatile",
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"حدث خطأ أثناء الاتصال بالذكاء الاصطناعي: {e}"

# 
st.markdown("""
    <div style="background-color:#1e1e1e; padding:15px; border-radius:10px; border-bottom: 4px solid #2e7d32; text-align:center;">
        <h2 style="color:white; margin:0;">الجامعة التقنية الوسطى - كلية البوليتكنك</h2>
        <p style="color:#4caf50; font-weight:bold; margin:5px;">مشروع طلاب شعبة E7:| علي نهاد | رؤى نديم | حسن محمد |</p>
    </div>
    """, unsafe_allow_html=True)

# القائمة الجانبية
app_mode = st.sidebar.selectbox("اختر المختبر الهندسي:", 
    ["مساعد المهندس الذكي (AI)", 
     "الأنظمة الرقمية والبوابات",
     "مختبر الدوائر (DC/AC/RC)", 
     "مختبر الدوال المثلثية",
     "مختبر السيجمويد (AI Math)", 
     "تحليل الدومين والرينج المتقدم"])

# 1. مساعد المهندس الذكي العام
if app_mode == "مساعد المهندس الذكي (AI)":
    st.header("🤖 مساعد المهندس الذكي العام")
    user_query = st.chat_input("اسأل عن أي مسألة هندسية أو رياضية...")
    if user_query:
        with st.chat_message("user"): st.write(user_query)
        with st.spinner("جاري التحليل..."):
            response = get_ai_explanation(user_query)
            with st.chat_message("assistant"): st.write(response)

# 2. الأنظمة الرقمية مع AI
elif app_mode == "الأنظمة الرقمية والبوابات":
    st.header("🔢 الأنظمة الرقمية والبوابات المنطقية")
    tab1, tab2 = st.tabs(["التحويل بين الأنظمة", "محاكاة البوابات"])
    
    with tab1:
        num = st.number_input("أدخل رقماً عشرياً:", min_value=0, value=10)
        st.write(f"الثنائي: {bin(num)}, الثماني: {oct(num)}, الستة عشري: {hex(num).upper()}")
        if st.button("اشرح لي خطوات التحويل"):
            st.info(get_ai_explanation(f"كيف يتم تحويل الرقم العشري {num} إلى ثنائي وثماني وستة عشري؟"))

    with tab2:
        gate = st.selectbox("البوابة:", ["AND", "OR", "XOR", "NAND", "NOR", "NOT"])
        a = st.radio("مدخل A", [0, 1], horizontal=True)
        b = st.radio("مدخل B", [0, 1], horizontal=True) if gate != "NOT" else None
        res = 0 # منطق البوابات
        if gate == "AND": res = a & b
        elif gate == "OR": res = a | b
        st.success(f"النتيجة: {res}")
        if st.button("اشرح عمل هذه البوابة"):
            st.info(get_ai_explanation(f"اشرح لي جدول الحقيقة (Truth Table) لبوابة {gate}."))

# 3. مختبر الدوائر مع AI
elif app_mode == "مختبر الدوائر (DC/AC/RC)":
    st.header("⚡ مختبر الدوائر الكهربائية")
    r1 = st.number_input("R1 (Ω)", value=10.0)
    v = st.number_input("الجهد (V)", value=12.0)
    if st.button("تحليل الدائرة بواسطة AI"):
        st.write(get_ai_explanation(f"دائرة كهربائية فيها جهد {v} فولت ومقاومة {r1} أوم، احسب التيار والقدرة واشرح القوانين."))

# 4. مختبر الدوال المثلثية مع AI
elif app_mode == "مختبر الدوال المثلثية":
    st.header("📐 الدوال المثلثية الستة")
    func = st.selectbox("الدالة:", ["sin", "cos", "tan", "cot", "sec", "csc"])
    deg = st.number_input("الزاوية بالدرجات:", value=45.0)
    if st.button("احسب واشرح بالخطوات"):
        st.write(get_ai_explanation(f"احسب قيمة {func}({deg}) بالخطوات مع توضيح موقعها في دائرة الوحدة."))

# 5. مختبر السيجمويد مع AI
elif app_mode == "مختبر السيجمويد (AI Math)":
    st.header("🧠 دالة السيجمويد والذكاء الاصطناعي")
    x_val = st.number_input("قيمة x:", value=0.0)
    if st.button("شرح الأهمية الرياضية"):
        st.write(get_ai_explanation(f"ما هي دالة السيجمويد؟ وكيف تحسب عند x={x_val}؟ وما علاقتها بالتعلم العميق؟"))

# 6. تحليل الدومين والرينج المتقدم (الميزة الكبرى)
elif app_mode == "تحليل الدومين والرينج المتقدم":
    st.header("📉 تحليل الدومين والرينج المتقدم")
    st.write("يمكنك كتابة الدالة كما في بايثون، مثال: `x**2` للتربيع، `np.sqrt(x)` للجذر، `1/x` للكسر.")
    
    formula = st.text_input("أدخل معادلة الدالة y = ", "x**2")
    x_min = st.number_input("بداية الدومين (x min):", value=-10.0)
    x_max = st.number_input("نهاية الدومين (x max):", value=10.0)
    
    try:
        x_vals = np.linspace(x_min, x_max, 500)
        # السماح باستخدام مكتبة numpy داخل الإدخال
        y_vals = eval(formula, {"x": x_vals, "np": np})
        
        fig = go.Figure(go.Scatter(x=x_vals, y=y_vals, mode='lines', name=f"y = {formula}"))
        fig.update_layout(template="plotly_dark", title=f"رسم الدالة: {formula}")
        st.plotly_chart(fig)
        
        if st.button("تحليل الدومين والرينج لهذه الدالة بواسطة AI"):
            with st.spinner("جاري التحليل الرياضي..."):
                prompt = f"حلل الدالة y = {formula} رياضياً. أوجد الدومين (Domain) والرينج (Range) واشرح إذا كان هناك إزاحة (Shift) أفقية أو عمودية بناءً على القواعد الرياضية."
                st.markdown(get_ai_explanation(prompt))
                
    except Exception as e:
        st.error(f"خطأ في صيغة الدالة: {e}. تأكد من كتابتها بشكل صحيح (مثلاً x**2 بدلاً من x^2).")

st.markdown("---")
st.write("الجامعة التقنية الوسطى - قسم الكترونيك والذكاء الاصطناعي - شعبة E7")





