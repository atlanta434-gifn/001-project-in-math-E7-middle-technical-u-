import streamlit as st
import numpy as np
import plotly.graph_objects as go
import google.generativeai as genai

# --- 1. ---
st.set_page_config(page_title="E7 Comprehensive Engineering Platform", layout="wide")

st.markdown("""
    <div style="background-color:#1e1e1e; padding:15px; border-radius:10px; border-bottom: 4px solid #2e7d32; text-align:center;">
        <h2 style="color:white; margin:0;">الجامعة التقنية الوسطى - </h2>
        <p style="color:#4caf50; font-weight:bold; margin:5px;">
            مشروع طلاب شعبة E7: 
            <span style="color:#bbb; font-weight:normal;">علي منتظر | عبدالله فراس | ايمن مصطفى | علي نهاد قادر | رؤى نديم كريم | | حسن محمد جاسم | حسين صباح نوري</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. القائمة الجانبية  ---
app_mode = st.sidebar.selectbox("اختر المختبر الهندسي:", 
    ["مساعد المهندس الذكي (AI)", 
     "الأنظمة الرقمية والبوابات",
     "مختبر الدوائر (DC/AC/RC)", 
     "مختبر الدوال المثلثية", 
     "مختبر السيجمويد (AI Math)", 
     "تحليل الدومين والرينج"])

# --- 3. شوكت يكمل الكود تعبت -_- ---
if app_mode == "مساعد المهندس الذكي (AI)":
    st.header("🤖 مساعد المهندس الذكي")
    
    # المفتاح المباشر
    api_key_direct = "AIzaSyBGEUIeCn0Vyob9tA254kNbrZrXjR9wmL4"
    
    try:
        genai.configure(api_key=api_key_direct)
        # تصحيح المسار الكامل للموديل لتجنب خطأ 404
        model = genai.GenerativeModel(model_name='models/gemini-1.5-flash')
        
        # هذا السطر يجب أن يكون بنفس مستوى محاذاة الموديل
        user_query = st.chat_input("دز اي شي تريده...")
        
        if user_query:
            with st.chat_message("user"):
                st.write(user_query)
            
            with st.spinner("جاري التحليل..."):
                # تأكد أن هذه الأسطر تبدأ بمسافة إضافية تحت spinner
                response = model.generate_content(f"أنت خبير هندسي لشعبة E7. أجب بالعربية: {user_query}")
                with st.chat_message("assistant"):
                    st.write(response.text)
    except Exception as e:
        st.error(f"حدث خطأ: {e}")
        
# --- 4. قسم المنطق الرقمي والبوابات  ---
elif app_mode == "الأنظمة الرقمية والبوابات":
    st.header("🔢 Digital Systems & Logic Gates")
    tab1, tab2 = st.tabs(["التحويل بين الأنظمة", "محاكاة البوابات المنطقية"])
    
    with tab1:
        num = st.number_input("أدخل رقماً عشرياً:", min_value=0, value=10)
        c1, c2, c3 = st.columns(3)
        c1.metric("Binary (ثنائي)", bin(num)[2:])
        c2.metric("Octal (ثماني)", oct(num)[2:])
        c3.metric("Hex (ستة عشري)", hex(num)[2:].upper())
        
    with tab2:
        gate = st.selectbox("اختر البوابة المنطقية:", ["AND", "OR", "XOR", "NAND", "NOR", "NOT"])
        col_a, col_b = st.columns(2)
        in_a = col_a.radio("Input A", [0, 1], horizontal=True)
        in_b = col_b.radio("Input B", [0, 1], horizontal=True) if gate != "NOT" else None
        
        if gate == "AND": res = in_a & in_b
        elif gate == "OR": res = in_a | in_b
        elif gate == "XOR": res = in_a ^ in_b
        elif gate == "NAND": res = 1 if not (in_a & in_b) else 0
        elif gate == "NOR": res = 1 if not (in_a | in_b) else 0
        elif gate == "NOT": res = 1 if in_a == 0 else 0
        
        st.markdown(f'<div style="text-align:center; padding:20px; border:2px solid #4caf50; border-radius:10px;"><h1 style="color:#4caf50;">Output: {res}</h1></div>', unsafe_allow_html=True)

# --- 5. مختبر الدوائر (Mixed DC/AC/RC) ---
elif app_mode == "مختبر الدوائر (DC/AC/RC)":
    mode = st.tabs(["DC Mixed (الربط المختلط)", "AC Circuits", "RC Transient"])
    with mode[0]:
        r1 = st.number_input("R1 (Series) Ω", value=10.0)
        r2 = st.number_input("R2 (Parallel 1) Ω", value=20.0)
        r3 = st.number_input("R3 (Parallel 2) Ω", value=20.0)
        v_s = st.number_input("Voltage Source (V)", value=12.0)
        r_eq = r1 + (r2*r3)/(r2+r3)
        st.success(f"المقاومة الكلية Req = {r_eq:.2f} Ω | التيار الكلي I = {(v_s/r_eq):.3f} A")
    with mode[1]:
        v_p = st.slider("Peak Voltage", 1, 311, 220)
        f = st.slider("Freq (Hz)", 1, 100, 50)
        t = np.linspace(0, 0.04, 500)
        v_ac = v_p * np.sin(2 * np.pi * f * t)
        st.plotly_chart(go.Figure(go.Scatter(x=t, y=v_ac, line=dict(color="#00d4ff"))).update_layout(template="plotly_dark", title="AC Sine Wave"))
    with mode[2]:
        r_val = st.number_input("R (Ω)", value=1000); c_val = st.number_input("C (μF)", value=100)*1e-6
        t_rc = np.linspace(0, 5*(r_val*c_val), 500)
        v_rc = 12 * (1 - np.exp(-t_rc/(r_val*c_val)))
        st.plotly_chart(go.Figure(go.Scatter(x=t_rc, y=v_rc)).update_layout(template="plotly_dark", title="RC Charging Curve"))

# --- 6. مختبر الدوال المثلثية الستة ---
elif app_mode == "مختبر الدوال المثلثية":
    st.header("📐 Trigonometric Functions (6 Functions)")
    f_type = st.selectbox("اختر الدالة:", ["sin", "cos", "tan", "cot", "sec", "csc"])
    ang = st.number_input("أدخل الزاوية (بالدرجات):", value=60.0)
    rad = np.radians(ang)
    try:
        if f_type == "sin": res = np.sin(rad)
        elif f_type == "cos": res = np.cos(rad)
        elif f_type == "tan": res = np.tan(rad)
        elif f_type == "cot": res = 1/np.tan(rad)
        elif f_type == "sec": res = 1/np.cos(rad)
        elif f_type == "csc": res = 1/np.sin(rad)
        st.success(f"النتيجة: {f_type}({ang}°) = {res:.4f}")
    except: st.error("قيمة غير معرفة")
    
    x_plot = np.arange(0, 361, 5)
    y_plot = np.sin(np.radians(x_plot)) # Default for visual
    fig = go.Figure(go.Scatter(x=x_plot, y=y_plot, mode='lines'))
    fig.update_layout(xaxis=dict(tickvals=[0, 60, 90, 120, 180, 270, 360]), template="plotly_dark")
    st.plotly_chart(fig)

# --- 7. مختبر السيجمويد ---
elif app_mode == "مختبر السيجمويد (AI Math)":
    st.header("🧠 Sigmoid Activation Function")
    x_in = st.number_input("أدخل قيمة x لحل المعادلة:", value=0.0)
    sig = 1 / (1 + np.exp(-x_in))
    st.latex(r"S(x) = \frac{1}{1 + e^{-x}}")
    st.metric(f"النتيجة عند x={x_in}", f"{sig:.4f}")
    
    x_range = np.linspace(-10, 10, 100)
    fig = go.Figure(go.Scatter(x=x_range, y=1/(1+np.exp(-x_range)), name="Sigmoid"))
    fig.add_trace(go.Scatter(x=[x_in], y=[sig], mode='markers', marker=dict(size=12, color='red'), name="Your Point"))
    st.plotly_chart(fig.update_layout(template="plotly_dark"))

# --- 8. تحليل الدومين والرينج ---
elif app_mode == "تحليل الدومين والرينج":
    st.header("📉 Domain & Range Analyzer")
    choice = st.selectbox("الدالة:", ["1/x", "sqrt(x)", "ln(x)"])
    a = st.slider("الإزاحة (a):", -5.0, 5.0, 0.0)
    x_vals = np.linspace(-10, 10, 500)
    if choice == "1/x":
        y_vals = 1/(x_vals - a); y_vals[np.abs(y_vals)>10] = np.nan
        st.info(f"Domain: x ≠ {a}")
    elif choice == "sqrt(x)":
        x_vals = x_vals[x_vals >= a]; y_vals = np.sqrt(x_vals - a)
        st.info(f"Domain: x ≥ {a}")
    st.plotly_chart(go.Figure(go.Scatter(x=x_vals, y=y_vals)).update_layout(template="plotly_dark"))

# --- Footer ---
st.markdown("---")
st.write("الجامعة التقنية الوسطى - كلية البوليتكنك - قسم تقنيات هندسة الالكترونيك والذكاء الاصطناعي - شعبة E7")





