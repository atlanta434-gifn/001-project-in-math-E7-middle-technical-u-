import streamlit as st
import numpy as np
import plotly.graph_objects as go
import google.generativeai as genai

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="E7 Engineering Platform", layout="wide")

# --- 2. الهوية البصرية (اللوغو والأسماء) ---
st.markdown("<div style='text-align: center;'><img src='https://studyiniraq.scrd-gate.gov.iq/studyiniraq/Images/mtu.png' width='120'></div>", unsafe_allow_html=True)
st.markdown("""
    <div style="background-color:#1e1e1e; padding:15px; border-radius:10px; border-bottom: 4px solid #2e7d32; text-align:center;">
        <h2 style="color:white; margin:0;">الجامعة التقنية الوسطى - شعبة E7</h2>
        <p style="color:#bbb;">إعداد: علي منتظر | عبدالله فراس | ايمن مصطفى | علي نهاد قادر | حسن محمد جاسم | حسين صباح نوري</p>
    </div>
    """, unsafe_allow_html=True)

# --- 3. القائمة الجانبية المتطورة ---
with st.sidebar:
    st.title("⚙️ الهندسة والذكاء")
    app_mode = st.selectbox("اختر القسم العملي:", 
        ["مساعد المهندس (AI)", "الدوائر الكهربائية (DC/AC/RC)", "تحليل الدوال المثلثية (6 الدوال)", 
         "الذكاء الاصطناعي (Sigmoid)", "الرياضيات (Domain & Range)"])

# --- 4. معالجة قسم المساعد الذكي (AI) - حل مشكلة الـ 404 ---
if app_mode == "مساعد المهندس (AI)":
    st.header("🤖 Engineering AI Assistant")
    if "GEMINI_API_KEY" in st.secrets:
        try:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            # تم تعديل اسم النموذج ليتوافق مع أحدث نسخة للمكتبة
            model = genai.GenerativeModel('gemini-pro') 
            user_msg = st.chat_input("اسألني عن الإلكترونيات أو حلول المسائل...")
            if user_msg:
                with st.chat_message("user"): st.write(user_msg)
                with st.spinner("جاري التحليل الهندسي..."):
                    prompt = f"أنت مهندس خبير صممتك شعبة E7 في الجامعة التقنية الوسطى. أجب باحترافية: {user_msg}"
                    response = model.generate_content(prompt)
                    with st.chat_message("assistant"): st.write(response.text)
        except Exception as e:
            st.error(f"خطأ في الاتصال: {e}")
    else:
        st.warning("يرجى التأكد من وضع GEMINI_API_KEY في Secrets")

# --- 5. قسم الدوائر الكهربائية المتطور (DC/AC/RC/Mixed) ---
elif app_mode == "الدوائر الكهربائية (DC/AC/RC)":
    st.header("⚡ Circuit Analysis (Mixed & Transient)")
    type_cir = st.radio("نوع الدائرة:", ["DC Mixed (Resistors)", "RC Transient", "AC Sine Wave"])
    
    if type_cir == "DC Mixed (Resistors)":
        st.write("حساب الربط المختلط (Series-Parallel)")
        r1 = st.number_input("R1 (Series)", value=100.0)
        r2 = st.number_input("R2 (Parallel 1)", value=200.0)
        r3 = st.number_input("R3 (Parallel 2)", value=200.0)
        v_in = st.number_input("Source Voltage (V)", value=12.0)
        
        r_parallel = (r2 * r3) / (r2 + r3)
        r_total = r1 + r_parallel
        i_total = v_in / r_total
        st.success(f"المقاومة الكلية: {r_total:.2f} Ω | التيار الكلي: {i_total:.4f} A")

    elif type_cir == "RC Transient":
        r = st.slider("Resistance (Ω)", 1000, 100000, 10000)
        c = st.slider("Capacitance (μF)", 1, 1000, 100) * 1e-6
        t = np.linspace(0, 5 * (r*c), 500)
        v_c = 12 * (1 - np.exp(-t/(r*c)))
        fig = go.Figure(go.Scatter(x=t, y=v_c, name="Charging Vc", line=dict(color="#00ffcc")))
        fig.update_layout(title="شحن المتسعة عبر الزمن", template="plotly_dark")
        st.plotly_chart(fig)

# --- 6. قسم الدوال المثلثية الستة مع الزوايا ---
elif app_mode == "تحليل الدوال المثلثية (6 الدوال)":
    st.header("📐 Trigonometric Analysis")
    func_type = st.selectbox("اختر الدالة:", ["sin", "cos", "tan", "cot", "sec", "csc"])
    
    # شبكة الزوايا المطلوبة (60, 90, 120...)
    angles_deg = np.arange(0, 361, 30)
    angles_rad = np.radians(angles_deg)
    
    # حساب القيم
    if func_type == "sin": y_vals = np.sin(angles_rad)
    elif func_type == "cos": y_vals = np.cos(angles_rad)
    elif func_type == "tan": y_vals = np.tan(angles_rad)
    elif func_type == "cot": y_vals = 1/np.tan(angles_rad)
    elif func_type == "sec": y_vals = 1/np.cos(angles_rad)
    elif func_type == "csc": y_vals = 1/np.sin(angles_rad)
    
    # الرسم البياني
    fig = go.Figure(go.Scatter(x=angles_deg, y=y_vals, mode='lines+markers', name=func_type))
    fig.update_layout(title=f"رسم دالة {func_type} مع زوايا المختبر", xaxis=dict(tickvals=angles_deg), template="plotly_dark")
    st.plotly_chart(fig)
    
    # جدول البيانات
    st.write("قيم الزوايا الدقيقة:")
    st.table({"الزاوية (Degree)": angles_deg, "القيمة": y_vals})

# --- 7. قسم السيجمويد وحل المسائل ---
elif app_mode == "الذكاء الاصطناعي (Sigmoid)":
    st.header("🧠 Neural Network Activation")
    st.subheader("حل مسألة Sigmoid")
    x_input = st.number_input("أدخل قيمة المدخل (x):", value=0.0)
    sigmoid_res = 1 / (1 + np.exp(-x_input))
    st.metric("النتيجة S(x)", f"{sigmoid_res:.4f}")
    
    # الرسم البياني للدالة
    x_range = np.linspace(-10, 10, 100)
    y_range = 1 / (1 + np.exp(-x_range))
    fig = go.Figure(go.Scatter(x=x_range, y=y_range, line=dict(color="yellow")))
    fig.add_trace(go.Scatter(x=[x_input], y=[sigmoid_res], mode='markers', marker=dict(size=15, color="red")))
    fig.update_layout(title="دالة السيجمويد مع تحديد نقطتك", template="plotly_dark")
    st.plotly_chart(fig)

# --- 8. قسم الدومين والرينج وحل المسائل ---
elif app_mode == "الرياضيات (Domain & Range)":
    st.header("📉 Domain & Range Solver")
    func_math = st.selectbox("اختر نوع الدالة للتحليل:", ["Rational (1/x)", "Square Root (√x)", "Logarithmic (ln)"])
    
    x = np.linspace(-10, 10, 400)
    if func_math == "Rational (1/x)":
        st.info("Domain: x ≠ 0 | Range: y ≠ 0")
        y = 1/x; y[np.abs(y)>10] = np.nan
    elif func_math == "Square Root (√x)":
        st.info("Domain: x ≥ 0 | Range: y ≥ 0")
        x = x[x>=0]; y = np.sqrt(x)
    
    fig = go.Figure(go.Scatter(x=x, y=y))
    fig.update_layout(title="تمثيل الدالة بيانياً", template="plotly_dark")
    st.plotly_chart(fig)

# --- Footer ---
st.markdown("---")
st.write("الجامعة التقنية الوسطى كلية البوليتكنك للتخصصات الهندسية قسم الكترونيك وذكاء اصطناعي شعبة E7")
