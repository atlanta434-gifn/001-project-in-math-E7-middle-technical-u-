import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time
import google.generativeai as genai

# --- 1. Page Configuration ---
st.set_page_config(page_title="MTU AI Project", layout="wide")

# إخفاء القوائم الافتراضية لزيادة الاحترافية والخصوصية
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 2. University Logo ---
st.markdown(
    """
    <div style="text-align: center; padding-bottom: 20px;">
        <img src="https://studyiniraq.scrd-gate.gov.iq/studyiniraq/Images/mtu.png" width="150">
    </div>
    """,
    unsafe_allow_html=True
)

# --- 3. Header Section (Official Branding) ---
st.markdown("""
    <div style="background-color:#1e1e1e; padding:15px; border-radius:10px; border-bottom: 4px solid #2e7d32; text-align:center;">
        <h2 style="color:white; margin:0;">الجامعة التقنية الوسطى</h2>
        <h4 style="color:#4caf50; margin:5px;">كلية البوليتكنك - قسم تقنيات هندسة الالكترونيك والذكاء الاصطناعي</h4>
        <p style="color:#bbb; margin:0;">إعداد الطلاب: علي منتظر | عبدالله فراس | ايمن مصطفى | علي نهاد قادر | حسن محمد جاسم | حسين صباح نوري</p>
    </div>
    """, unsafe_allow_html=True)

# --- 4. Sidebar Navigation ---
st.sidebar.title("Project Modules")
app_mode = st.sidebar.selectbox("Select Module:", 
    ["محاكاة الدوائر dc", "الدومن والرينج", "الأنظمة الرقمية والبوابات المنطقية", "الدوال المثلثية بالهيرتز", "رسم دالة السيجمويد", "مساعد المهندس الذكي (AI)"])

# --- 5. Modules Logic ---

if app_mode == "محاكاة الدوائر dc":
    st.subheader("RC Circuit Transient Analysis")
    c1, c2 = st.columns([1, 3])
    with c1:
        [span_3](start_span)v0 = st.number_input("V_initial (Volts):", 0.0, 24.0, 5.0)[span_3](end_span)
        [span_4](start_span)res = st.slider("Resistance (Ohms):", 1000, 50000, 10000)[span_4](end_span)
        [span_5](start_span)cap = st.slider("Capacitance (uF):", 10, 1000, 470) * 1e-6[span_5](end_span)
        [span_6](start_span)tau = res * cap[span_6](end_span)
        [span_7](start_span)run_btn = st.button("Simulate Discharge")[span_7](end_span)

    if run_btn:
        [span_8](start_span)t = np.linspace(0, tau*5, 120)[span_8](end_span)
        [span_9](start_span)v = v0 * np.exp(-t/tau)[span_9](end_span)
        [span_10](start_span)chart = st.empty()[span_10](end_span)
        for i in range(1, len(t), 2):
            [span_11](start_span)fig = go.Figure(go.Scatter(x=t[:i], y=v[:i], mode='lines', line=dict(color='#00ffcc')))[span_11](end_span)
            [span_12](start_span)fig.update_layout(template="plotly_dark", xaxis_title="Time (s)", yaxis_title="Voltage (V)")[span_12](end_span)
            [span_13](start_span)chart.plotly_chart(fig, use_container_width=True)[span_13](end_span)
            [span_14](start_span)time.sleep(0.01)[span_14](end_span)

elif app_mode == "الدومن والرينج":
    st.subheader("Interactive Domain and Range Analysis (Stewart Calculus)")
    [span_15](start_span)x_range = st.slider("Select X-axis Limits:", -20.0, 20.0, (-10.0, 10.0))[span_15](end_span)
    [span_16](start_span)func_select = st.selectbox("Select Function:", ["1/x", "sqrt(x)", "ln(x)"])[span_16](end_span)
    [span_17](start_span)x = np.linspace(x_range[0], x_range[1], 1000)[span_17](end_span)
    
    if func_select == "1/x":
        [span_18](start_span)x = x[x != 0]; y = 1/x[span_18](end_span)
        [span_19](start_span)st.success(f"Domain: ({x_range[0]}, 0) U (0, {x_range[1]})")[span_19](end_span)
    elif func_select == "sqrt(x)":
        [span_20](start_span)x = x[x >= 0]; y = np.sqrt(x)[span_20](end_span)
        [span_21](start_span)st.success(f"Domain: [0, {x_range[1]}]")[span_21](end_span)
    elif func_select == "ln(x)":
        [span_22](start_span)x = x[x > 0]; y = np.log(x)[span_22](end_span)
        [span_23](start_span)st.success(f"Domain: (0, {x_range[1]}]")[span_23](end_span)

    [span_24](start_span)fig = go.Figure(go.Scatter(x=x, y=y, line=dict(color='#ff007f', width=3)))[span_24](end_span)
    [span_25](start_span)fig.update_layout(template="plotly_dark", xaxis_title="x", yaxis_title="f(x)")[span_25](end_span)
    [span_26](start_span)st.plotly_chart(fig, use_container_width=True)[span_26](end_span)

elif app_mode == "الدوال المثلثية بالهيرتز":
    st.subheader("Trigonometric Waveforms")
    [span_27](start_span)trig_func = st.radio("Function:", ["Sin", "Cos", "Tan"], horizontal=True)[span_27](end_span)
    [span_28](start_span)freq = st.slider("Frequency (Hz):", 1, 10, 2)[span_28](end_span)
    [span_29](start_span)t = np.linspace(0, 2, 500)[span_29](end_span)
    [span_30](start_span)if trig_func == "Sin": y = np.sin(2 * np.pi * freq * t)[span_30](end_span)
    [span_31](start_span)elif trig_func == "Cos": y = np.cos(2 * np.pi * freq * t)[span_31](end_span)
    else:
        [span_32](start_span)y = np.tan(2 * np.pi * freq * t)[span_32](end_span)
        [span_33](start_span)y[np.abs(y) > 5] = np.nan[span_33](end_span)
    [span_34](start_span)fig = go.Figure(go.Scatter(x=t, y=y))[span_34](end_span)
    [span_35](start_span)fig.update_layout(template="plotly_dark", yaxis_range=[-2, 2])[span_35](end_span)
    [span_36](start_span)st.plotly_chart(fig, use_container_width=True)[span_36](end_span)

elif app_mode == "رسم دالة السيجمويد":
    st.subheader("Activation Functions in AI")
    [span_37](start_span)st.markdown("The Sigmoid function $S(x) = \\frac{1}{1 + e^{-x}}$ is essential for Neural Networks.")[span_37](end_span)
    [span_38](start_span)x_ai = np.linspace(-10, 10, 200)[span_38](end_span)
    [span_39](start_span)y_ai = 1 / (1 + np.exp(-x_ai))[span_39](end_span)
    [span_40](start_span)fig = go.Figure(go.Scatter(x=x_ai, y=y_ai, line=dict(color='#ffff00')))[span_40](end_span)
    [span_41](start_span)fig.update_layout(template="plotly_dark", title="Sigmoid Activation Function")[span_41](end_span)
    [span_42](start_span)st.plotly_chart(fig, use_container_width=True)[span_42](end_span)

elif app_mode == "الأنظمة الرقمية والبوابات المنطقية":
    [span_43](start_span)st.header("الأنظمة الرقمية والبوابات المنطقية")[span_43](end_span)
    [span_44](start_span)tab1, tab2 = st.tabs(["التحويل بين الأنظمة", "محاكاة البوابات المنطقية"])[span_44](end_span)
    with tab1:
        [span_45](start_span)num_input = st.number_input("Enter Decimal Number:", min_value=0, value=10)[span_45](end_span)
        [span_46](start_span)c1, c2, c3 = st.columns(3)[span_46](end_span)
        [span_47](start_span)c1.metric("Binary", bin(num_input)[2:])[span_47](end_span)
        [span_48](start_span)c2.metric("Octal", oct(num_input)[2:])[span_48](end_span)
        [span_49](start_span)c3.metric("Hexadecimal", hex(num_input)[2:].upper())[span_49](end_span)
    with tab2:
        [span_50](start_span)gate_type = st.selectbox("Select Logic Gate:", ["AND", "OR", "XOR", "NAND", "NOR"])[span_50](end_span)
        [span_51](start_span)col_a, col_b = st.columns(2)[span_51](end_span)
        [span_52](start_span)input_a = col_a.radio("Input A", [0, 1], horizontal=True)[span_52](end_span)
        [span_53](start_span)input_b = col_b.radio("Input B", [0, 1], horizontal=True)[span_53](end_span)
        [span_54](start_span)if gate_type == "AND": result = input_a & input_b[span_54](end_span)
        [span_55](start_span)elif gate_type == "OR": result = input_a | input_b[span_55](end_span)
        [span_56](start_span)elif gate_type == "XOR": result = input_a ^ input_b[span_56](end_span)
        [span_57](start_span)elif gate_type == "NAND": result = 1 if not (input_a & input_b) else 0[span_57](end_span)
        [span_58](start_span)elif gate_type == "NOR": result = 1 if not (input_a | input_b) else 0[span_58](end_span)
        [span_59](start_span)st.markdown(f'<div style="text-align:center; padding:20px; border:2px solid #4caf50; border-radius:10px;"><h1 style="color:#4caf50;">Output: {result}</h1></div>', unsafe_allow_html=True)[span_59](end_span)

# --- القسم الجديد: مساعد المهندس الذكي (AI) ---
elif app_mode == "مساعد المهندس الذكي (AI)":
    st.header("Engineering AI Assistant")
    try:
        # استدعاء المفتاح سرياً من إعدادات الموقع
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        user_msg = st.chat_input("Ask about Electronics, AI, or Math...")
        if user_msg:
            with st.chat_message("user"):
                st.write(user_msg)
            with st.spinner("Analyzing request..."):
                system_context = (
                    "أنت مهندس خبير ومساعد ذكي صممتك 'شعبة E7' "
                    "من قسم تقنيات هندسة الالكترونيك والذكاء الاصطناعي في MTU. "
                    "يجب أن تكون إجاباتك تقنية ودقيقة وباللغة العربية. "
                )
                response = model.generate_content(system_context + user_msg)
                with st.chat_message("assistant"):
                    st.write(response.text)
    except Exception as e:
        st.warning("الرجاء التأكد من إعداد GEMINI_API_KEY في Secrets.")

# --- Footer ---
st.markdown("---")
st.write("الجامعة التقنية الوسطى - كلية البوليتكنك - شعبة E7")





