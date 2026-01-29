import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

# --- Page Configuration ---
st.set_page_config(page_title="MTU AI Project", layout="wide")

# --- Header Section (Official Branding) ---
st.markdown("""
    <div style="background-color:#1e1e1e; padding:15px; border-radius:10px; border-bottom: 4px solid #2e7d32; text-align:center;">
        <h2 style="color:white; margin:0;">الجامعة التقنية الوسطى</h2>
        <h4 style="color:#4caf50; margin:5px;">كلية البوليتكنك - قسم تقنيات هندسة الالكترونيك والذكاء الاصطناعي</h4>
        <p style="color:#bbb; margin:0;">إعداد الطلاب: علي نهاد قادر | حسن محمد جاسم | حسين صباح نوري</p>
    </div>
    """, unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("Project Modules")
app_mode = st.sidebar.selectbox("Select Module:", 
    ["Circuit Simulation", "Calculus: Domain & Range", "Trigonometric Functions", "AI Sigmoid Logic"])

# --- 1. Kirchhoff RC Circuit Module ---
if app_mode == "Circuit Simulation":
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

# --- 2. Calculus Stewart Module (Domain & Range) ---
elif app_mode == "Calculus: Domain & Range":
    st.subheader("Domain and Range Analysis (Stewart Calculus)")
    func_select = st.selectbox("Select Function:", ["1/x", "sqrt(x)", "ln(x)"])
    
    x = np.linspace(-10, 10, 500)
    if func_select == "1/x":
        x = x[x != 0]; y = 1/x
        st.code("Domain: (-∞, 0) U (0, ∞) | Range: (-∞, 0) U (0, ∞)")
    elif func_select == "sqrt(x)":
        x = np.linspace(0, 10, 500); y = np.sqrt(x)
        st.code("Domain: [0, ∞) | Range: [0, ∞)")
    else:
        x = np.linspace(0.1, 10, 500); y = np.log(x)
        st.code("Domain: (0, ∞) | Range: (-∞, ∞)")

    fig = go.Figure(go.Scatter(x=x, y=y, name=func_select))
    fig.update_layout(template="plotly_dark", xaxis_title="x", yaxis_title="f(x)")
    st.plotly_chart(fig, use_container_width=True)

# --- 3. Trigonometric Module ---
elif app_mode == "Trigonometric Functions":
    st.subheader("Trigonometric Waveforms")
    trig_func = st.radio("Function:", ["Sin", "Cos", "Tan"], horizontal=True)
    freq = st.slider("Frequency (Hz):", 1, 10, 2)
    
    t = np.linspace(0, 2, 500)
    if trig_func == "Sin":
        y = np.sin(2 * np.pi * freq * t)
    elif trig_func == "Cos":
        y = np.cos(2 * np.pi * freq * t)
    else:
        y = np.tan(2 * np.pi * freq * t)
        y[np.abs(y) > 5] = np.nan # Clean tan peaks

    fig = go.Figure(go.Scatter(x=t, y=y))
    fig.update_layout(template="plotly_dark", yaxis_range=[-2, 2])
    st.plotly_chart(fig, use_container_width=True)

# --- 4. AI & Sigmoid Module ---
elif app_mode == "AI Sigmoid Logic":
    st.subheader("Activation Functions in AI")
    st.markdown("The Sigmoid function $S(x) = \\frac{1}{1 + e^{-x}}$ is essential for Neural Networks.")
    
    x_ai = np.linspace(-10, 10, 200)
    y_ai = 1 / (1 + np.exp(-x_ai))
    
    fig = go.Figure(go.Scatter(x=x_ai, y=y_ai, line=dict(color='#ffff00')))
    fig.update_layout(template="plotly_dark", title="Sigmoid Activation Function")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.write("الجامعة التقنية الوسطى كلية بوليتكنك قسم تقنيات هندسة الالكترونيك والذكاء الاصطناعي شعبة 7")


