import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time
import google.generativeai as genai

# --- Configuration & Styling ---
st.set_page_config(page_title="MTU AI Project", layout="wide")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- Logo & Branding ---
st.markdown("<div style='text-align: center; padding-bottom: 20px;'><img src='https://studyiniraq.scrd-gate.gov.iq/studyiniraq/Images/mtu.png' width='150'></div>", unsafe_allow_html=True)

st.markdown("""
    <div style="background-color:#1e1e1e; padding:15px; border-radius:10px; border-bottom: 4px solid #2e7d32; text-align:center;">
        <h2 style="color:white; margin:0;">الجامعة التقنية الوسطى</h2>
        <h4 style="color:#4caf50; margin:5px;">كلية البوليتكنك - قسم تقنيات هندسة الالكترونيك والذكاء الاصطناعي</h4>
        <p style="color:#bbb; margin:0;">إعداد طلاب شعبة E7: علي منتظر | عبدالله فراس | ايمن مصطفى | علي نهاد قادر | حسن محمد jاسم | حسين صباح نوري</p>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.title("Project Modules")
app_mode = st.sidebar.selectbox("Select Module:", 
    ["محاكاة الدوائر dc", "الدومن والرينج", "الأنظمة الرقمية والبوابات المنطقية", 
     "الدوال المثلثية بالهيرتز", "رسم دالة السيجمويد", "مساعد المهندس الذكي (AI)"])

# --- Modules Execution ---

if app_mode == "محاكاة الدوائر dc":
    st.subheader("RC Circuit Transient Analysis")
    c1, c2 = st.columns([1, 3])
    with c1:
        v0 = st.number_input("V_initial (Volts):", 0.0, 24.0, 5.0)
        res = st.slider("Resistance (Ohms):", 1000, 50000, 10000)
        cap = st.slider("Capacitance (uF):", 10, 1000, 470) * 1e-6
        tau = res * cap
        run_btn = st.button("Simulate Discharge")
    if run_btn:
        t = np.linspace(0, tau*5, 120)
        v = v0 * np.exp(-t/tau)
        chart = st.empty()
        for i in range(1, len(t), 2):
            fig = go.Figure(go.Scatter(x=t[:i], y=v[:i], mode='lines', line=dict(color='#00ffcc')))
            fig.update_layout(template="plotly_dark", xaxis_title="Time (s)", yaxis_title="Voltage (V)")
            chart.plotly_chart(fig, use_container_width=True)
            time.sleep(0.01)

elif app_mode == "الدومن والرينج":
    st.subheader("Interactive Domain and Range Analysis")
    x_range = st.slider("Select X-axis Limits:", -20.0, 20.0, (-10.0, 10.0))
    func_select = st.selectbox("Select Function:", ["1/x", "sqrt(x)", "ln(x)"])
    x = np.linspace(x_range[0], x_range[1], 1000)
    if func_select == "1/x":
        x = x[x != 0]; y = 1/x
        st.success(f"Domain: ({x_range[0]}, 0) U (0, {x_range[1]})")
    elif func_select == "sqrt(x)":
        x = x[x >= 0]; y = np.sqrt(x)
        st.success(f"Domain: [0, {x_range[1]}]")
    elif func_select == "ln(x)":
        x = x[x > 0]; y = np.log(x)
        st.success(f"Domain: (0, {x_range[1]}]")
    fig = go.Figure(go.Scatter(x=x, y=y, line=dict(color='#ff007f', width=3)))
    fig.update_layout(template="plotly_dark", xaxis_title="x", yaxis_title="f(x)")
    st.plotly_chart(fig, use_container_width=True)

elif app_mode == "الأنظمة الرقمية والبوابات المنطقية":
    st.header("الأنظمة الرقمية والبوابات المنطقية")
    tab1, tab2 = st.tabs(["التحويل بين الأنظمة", "محاكاة البوابات المنطقية"])
    with tab1:
        num_input = st.number_input("Enter Decimal Number:", min_value=0, value=10)
        c1, c2, c3 = st.columns(3)
        c1.metric("Binary", bin(num_input)[2:])
        c2.metric("Octal", oct(num_input)[2:])
        c3.metric("Hexadecimal", hex(num_input)[2:].upper())
    with tab2:
        gate_type = st.selectbox("Select Logic Gate:", ["AND", "OR", "XOR", "NAND", "NOR"])
        col_a, col_b = st.columns(2)
        input_a = col_a.radio("Input A", [0, 1], horizontal=True)
        input_b = col_b.radio("Input B", [0, 1], horizontal=True)
        if gate_type == "AND": result = input_a & input_b
        elif gate_type == "OR": result = input_a | input_b
        elif gate_type == "XOR": result = input_a ^ input_b
        elif gate_type == "NAND": result = 1 if not (input_a & input_b) else 0
        elif gate_type == "NOR": result = 1 if not (input_a | input_b) else 0
        st.markdown(f'<div style="text-align:center; padding:20px; border:2px solid #4caf50; border-radius:10px;"><h1 style="color:#4caf50;">Output: {result}</h1></div>', unsafe_allow_html=True)

elif app_mode == "الدوال المثلثية بالهيرتز":
    st.subheader("Trigonometric Waveforms")
    freq = st.slider("Frequency (Hz):", 1, 10, 2)
    t = np.linspace(0, 2, 500)
    y = np.sin(2 * np.pi * freq * t)
    fig = go.Figure(go.Scatter(x=t, y=y, line=dict(color='#00d4ff')))
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

elif app_mode == "رسم دالة السيجمويد":
    st.subheader("Sigmoid Activation Function")
    x = np.linspace(-10, 10, 200)
    y = 1 / (1 + np.exp(-x))
    fig = go.Figure(go.Scatter(x=x, y=y, line=dict(color='#ffff00')))
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

elif app_mode == "مساعد المهندس الذكي (AI)":
    st.header("Engineering AI Assistant")
    if "GEMINI_API_KEY" in st.secrets:
        try:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            model = genai.GenerativeModel('gemini-1.5-flash')
            user_msg = st.chat_input("Ask about Electronics or AI...")
            if user_msg:
                with st.chat_message("user"): st.write(user_msg)
                with st.spinner("Analyzing..."):
                    prompt = f"أنت مهندس خبير ومساعد ذكي صممتك 'شعبة E7' من قسم هندسة الالكترونيك والذكاء الاصطناعي في MTU. أجب بالعربية على: {user_msg}"
                    response = model.generate_content(prompt)
                    with st.chat_message("assistant"): st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("الرجاء إعداد مفتاح الـ API في الـ Secrets لتفعيل المحادثة.")

st.markdown("---")
st.write("الجامعة التقنية الوسطى - كلية البوليتكنك - قسم تقنيات هندسة الالكترونيك والذكاء الاصطناعي - شعبة E7")
