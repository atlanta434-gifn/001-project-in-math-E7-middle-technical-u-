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
        <p style="color:#bbb; margin:0;">إعداد الطلاب: علي منتظر | عبدالله فراس | ايمن مصطفى | علي نهاد قادر | حسن محمد جاسم | حسين صباح نوري</p>
    </div>
    """, unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("Project Modules")
app_mode = st.sidebar.selectbox("Select Module:", 
    ["محاكاة الدوائر dc", "الدومن والرينج", "الأنظمة الرقمية والبوابات المنطقية", "الدوال المثلثية بالهيرتز", "رسم دالة السيجمويد"])

# --- 1. كيرشوف rc ---
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

# --- 2. الدومن والرينج  ---
if app_mode == "الدومن والرينج":
    st.subheader("Interactive Domain and Range Analysis (Stewart Calculus)")
    
    # إضافة سلايدر للتحكم في قيم المحور X
    x_range = st.slider("Select X-axis Limits:", -20.0, 20.0, (-10.0, 10.0))
    func_select = st.selectbox("Select Function:", ["1/x", "sqrt(x)", "ln(x)"])
    
    # توليد القيم بناءً على السلايدر
    x = np.linspace(x_range[0], x_range[1], 1000)
    
    if func_select == "1/x":
        x = x[x != 0] 
        y = 1/x
        st.success(f"Domain: ({x_range[0]}, 0) U (0, {x_range[1]})")
        st.info("Range: (-∞, 0) U (0, ∞)")
        
    elif func_select == "sqrt(x)":
        x = x[x >= 0] 
        y = np.sqrt(x)
        st.success(f"Domain: [0, {x_range[1]}]")
        st.info(f"Range: [0, {np.sqrt(max(0, x_range[1])):.2f}]")
        
    elif func_select == "ln(x)":
        x = x[x > 0] 
        y = np.log(x)
        st.success(f"Domain: (0, {x_range[1]}]")
        st.info(f"Range: (-∞, {np.log(max(0.1, x_range[1])):.2f}]")

    fig = go.Figure(go.Scatter(x=x, y=y, line=dict(color='#ff007f', width=3)))
    fig.update_layout(template="plotly_dark", xaxis_title="x", yaxis_title="f(x)")
    st.plotly_chart(fig, use_container_width=True)

# --- 3. الدالة المثلثية ---
elif app_mode == "الدوال المثلثية بالهيرتز":
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

# --- 4. دالة السيجمويد ---
elif app_mode == "رسم دالة السيجمويد":
    st.subheader("Activation Functions in AI")
    st.markdown("The Sigmoid function $S(x) = \\frac{1}{1 + e^{-x}}$ is essential for Neural Networks.")
    
    x_ai = np.linspace(-10, 10, 200)
    y_ai = 1 / (1 + np.exp(-x_ai))
    
    fig = go.Figure(go.Scatter(x=x_ai, y=y_ai, line=dict(color='#ffff00')))
    fig.update_layout(template="plotly_dark", title="Sigmoid Activation Function")
    st.plotly_chart(fig, use_container_width=True)

# --- 5. الأنظمة الرقمية والبوابات المنطقية ---
elif app_mode == "الأنظمة الرقمية والبوابات المنطقية":
    st.header("الأنظمة الرقمية والبوابات المنطقية")
    
    tab1, tab2 = st.tabs(["التحويل بين الأنظمة", "محاكاة البوابات المنطقية"])
    
    with tab1:
        st.subheader("Number Systems Converter")
        num_input = st.number_input("Enter Decimal Number:", min_value=0, value=10)
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Binary", bin(num_input)[2:])
        c2.metric("Octal", oct(num_input)[2:])
        c3.metric("Hexadecimal", hex(num_input)[2:].upper())
        
    with tab2:
        st.subheader("Logic Gates Simulator")
        gate_type = st.selectbox("Select Logic Gate:", ["AND", "OR", "XOR", "NAND", "NOR"])
        
        col_a, col_b = st.columns(2)
        input_a = col_a.radio("Input A", [0, 1], horizontal=True)
        input_b = col_b.radio("Input B", [0, 1], horizontal=True)
        
        # Logic Calculation
        if gate_type == "AND": result = input_a & input_b
        elif gate_type == "OR": result = input_a | input_b
        elif gate_type == "XOR": result = input_a ^ input_b
        elif gate_type == "NAND": result = 1 if not (input_a & input_b) else 0
        elif gate_type == "NOR": result = 1 if not (input_a | input_b) else 0
        
        # Display Result
        st.markdown(f"""
            <div style="text-align:center; padding:20px; border:2px solid #4caf50; border-radius:10px;">
                <h1 style="color:#4caf50;">Output: {result}</h1>
                <p style="color:#888;">{input_a} {gate_type} {input_b} = {result}</p>
            </div>
        """, unsafe_allow_html=True)

        # Logic Table Visualization
        st.write("Truth Table View:")
        labels = ['A', 'B', 'Output']
        values = [input_a, input_b, result]
        fig_gate = go.Figure(data=[go.Bar(x=labels, y=values, marker_color=['#00d4ff', '#00d4ff', '#ff007f'])])
        fig_gate.update_layout(template="plotly_dark", yaxis_range=[0, 1.2], height=300)
        st.plotly_chart(fig_gate, use_container_width=True)

st.markdown("---")
st.write("الجامعة التقنية الوسطى كلية بوليتكنك قسم تقنيات هندسة الالكترونيك والذكاء الاصطناعي شعبة 7")





