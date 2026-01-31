import streamlit as st
import numpy as np
import plotly.graph_objects as go
import google.generativeai as genai

# --- 1. ---
st.markdown("""
    <div style="background-color:#1e1e1e; padding:15px; border-radius:10px; border-bottom: 4px solid #2e7d32; text-align:center;">
        <h2 style="color:white; margin:0;">الجامعة التقنية الوسطى - </h2>
        <p style="color:#4caf50; font-weight:bold; margin:5px;">
            مشروع طلاب شعبة E7: 
            <span style="color:#bbb; font-weight:normal;">علي منتظر | عبدالله فراس | ايمن مصطفى | علي نهاد قادر | حسن محمد جاسم | حسين صباح نوري</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. القائمة الجانبية ---
app_mode = st.sidebar.selectbox("اختر المختبر الهندسي:", 
    ["مساعد المهندس الذكي (AI)", "مختبر الدوائر (DC/AC/RC)", "مختبر الدوال المثلثية", "مختبر السيجمويد (AI Math)", "تحليل الدومين والرينج"])

# --- 3.  ---
if app_mode == "مساعد المهندس الذكي (AI)":
    st.header("🤖 مساعد المهندس الذكي")
    if "GEMINI_API_KEY" in st.secrets:
        try:
            # شوكت يكمل كود والله تعب -_-
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
           model = genai.GenerativeModel('gemini-1.5-flash-latest')
            
            user_query = st.chat_input("اسأل عن الدوائر، المعادلات، أو نظريات الذكاء الاصطناعي...")
            if user_query:
                with st.chat_message("user"): st.write(user_query)
                with st.spinner("جاري المعالجة..."):
                    # 
                    response = model.generate_content(f"أنت خبير هندسي لشعبة E7. أجب بالعربية: {user_query}")
                    with st.chat_message("assistant"): st.write(response.text)
        except Exception as e:
            st.error(f"خطأ في الاتصال: تأكد من صلاحية المفتاح أو جرب تحديث الصفحة. (تفاصيل: {e})")
    else:
        st.warning("يرجى وضع GEMINI_API_KEY في إعدادات Secrets.")

# --- 4. مختبر الدوائر المتكامل (تفعيل AC) ---
elif app_mode == "مختبر الدوائر (DC/AC/RC)":
    st.header("⚡ Circuit Analysis Lab")
    mode = st.tabs(["DC Mixed", "AC Circuits", "RC Transient"])
    
    with mode[0]: # DC Mixed
        st.subheader("الربط المختلط (Series-Parallel)")
        col1, col2 = st.columns(2)
        r1 = col1.number_input("R1 (Series) Ω", value=10.0)
        r2 = col1.number_input("R2 (Parallel) Ω", value=20.0)
        r3 = col2.number_input("R3 (Parallel) Ω", value=20.0)
        vin = col2.number_input("Voltage Source (V)", value=12.0)
        
        req = r1 + (r2*r3)/(r2+r3)
        st.metric("المقاومة الكلية Req", f"{req:.2f} Ω")
        st.metric("التيار الكلي Itotal", f"{(vin/req):.3f} A")

    with mode[1]: # AC Circuits (تم تفعيله)
        st.subheader("تحليل دوائر التيار المتناوب AC")
        v_peak = st.slider("Peak Voltage (Vm)", 1, 311, 220)
        freq = st.slider("Frequency (Hz)", 1, 100, 50)
        t = np.linspace(0, 0.04, 500)
        v_ac = v_peak * np.sin(2 * np.pi * freq * t)
        
        fig = go.Figure(go.Scatter(x=t, y=v_ac, name="AC Voltage", line=dict(color="#00d4ff")))
        fig.update_layout(title="موجة الجيب المتناوبة", xaxis_title="Time (s)", yaxis_title="Voltage (V)", template="plotly_dark")
        st.plotly_chart(fig)
        st.write(f"V_rms ≈ {v_peak * 0.707:.2f} V")

    with mode[2]: # RC Transient
        st.write("شحن وتفريغ المتسعة")
        r_val = st.number_input("Resistance Ω", value=1000)
        c_val = st.number_input("Capacitance μF", value=100) * 1e-6
        tau = r_val * c_val
        t_rc = np.linspace(0, 5*tau, 500)
        v_rc = 12 * (1 - np.exp(-t_rc/tau))
        st.plotly_chart(go.Figure(go.Scatter(x=t_rc, y=v_rc)).update_layout(template="plotly_dark"))

# --- 5. مختبر الدوال المثلثية (تغيير القيم والزوايا) ---
elif app_mode == "مختبر الدوال المثلثية":
    st.header("📐 Trigonometric Functions Lab")
    f_type = st.selectbox("اختر الدالة:", ["sin", "cos", "tan", "cot", "sec", "csc"])
    custom_angle = st.number_input("أدخل زاوية معينة لحسابها (درجة):", value=60.0)
    
    # حساب قيمة الزاوية المدخلة
    rad = np.radians(custom_angle)
    try:
        if f_type == "sin": res = np.sin(rad)
        elif f_type == "cos": res = np.cos(rad)
        elif f_type == "tan": res = np.tan(rad)
        elif f_type == "cot": res = 1/np.tan(rad)
        elif f_type == "sec": res = 1/np.cos(rad)
        elif f_type == "csc": res = 1/np.sin(rad)
        st.success(f"قيمة {f_type}({custom_angle}°) = {res:.4f}")
    except: st.error("قيمة غير معرفة لهذه الزاوية")

    # رسم الموجة مع زوايا محددة (60, 90, 120...)
    angles = np.arange(0, 361, 10)
    y_plot = np.sin(np.radians(angles)) # افتراضي sin للرسم
    fig = go.Figure(go.Scatter(x=angles, y=y_plot, mode='lines+markers'))
    fig.update_layout(xaxis=dict(tickvals=[0, 60, 90, 120, 180, 270, 360]), template="plotly_dark")
    st.plotly_chart(fig)

# --- 6. مختبر السيجمويد (حل مسائل تفاعلي) ---
elif app_mode == "مختبر السيجمويد (AI Math)":
    st.header("🧠 Sigmoid Solver")
    val_x = st.number_input("أدخل قيمة x لحل المسألة:", value=1.0)
    s_x = 1 / (1 + np.exp(-val_x))
    
    st.latex(r"S(x) = \frac{1}{1 + e^{-x}}")
    st.metric(f"النتيجة لـ x={val_x}", f"{s_x:.4f}")
    
    x_range = np.linspace(-10, 10, 100)
    y_range = 1 / (1 + np.exp(-x_range))
    fig = go.Figure(go.Scatter(x=x_range, y=y_range))
    fig.add_trace(go.Scatter(x=[val_x], y=[s_x], mode='markers', marker=dict(size=12, color='red'), name="Your Point"))
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig)

# --- 7. تحليل الدومين والرينج (تفاعلي) ---
elif app_mode == "تحليل الدومين والرينج":
    st.header("📉 Domain & Range Analyzer")
    func_choice = st.selectbox("الدالة:", ["1/x", "sqrt(x)", "ln(x)"])
    shift = st.slider("إزاحة الدالة (x - a):", -5.0, 5.0, 0.0)
    
    x_domain = np.linspace(-10, 10, 500)
    if func_choice == "1/x":
        y_domain = 1/(x_domain - shift)
        y_domain[np.abs(y_domain) > 10] = np.nan
        st.info(f"Domain: x ≠ {shift}")
    elif func_choice == "sqrt(x)":
        x_domain = x_domain[x_domain >= shift]
        y_domain = np.sqrt(x_domain - shift)
        st.info(f"Domain: x ≥ {shift}")
    
    st.plotly_chart(go.Figure(go.Scatter(x=x_domain, y=y_domain)).update_layout(template="plotly_dark"))

# --- Footer ---
st.markdown("---")
st.write("الجامعة التقنية الوسطى كلية البوليتكنك قسم الالكترونيك والذكاء الاصطناعي شعبةE7")






