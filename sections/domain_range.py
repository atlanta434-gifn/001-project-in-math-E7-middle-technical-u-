import streamlit as st
import numpy as np
import plotly.graph_objects as go
from utils import section_header, get_ai_explanation

def show():
    section_header("المجال والمدى", "تحليل الدوال والتمثيل البياني")
    
    func_str = st.text_input("أدخل الدالة (مثال: 1/x, sqrt(x), sin(x)):", "sin(x)")
    
    if st.button("تحليل الدالة"):
        with st.spinner("جاري التحليل..."):
            explanation = get_ai_explanation(f"Calculate the domain and range of the function: f(x) = {func_str}. Explain why.")
            st.markdown(explanation)
            
    st.divider()
    st.subheader("التمثيل البياني")
    plot_type = st.selectbox("نوع الرسم:", ["Linear (خطي)", "Polar (قطبي)", "Circular (دائري)"])
    
    x = np.linspace(-10, 10, 400)
    # Basic safe evaluation for plotting
    try:
        # Replace common math functions for numpy
        safe_func = func_str.replace('sin', 'np.sin').replace('cos', 'np.cos').replace('tan', 'np.tan').replace('sqrt', 'np.sqrt').replace('exp', 'np.exp').replace('log', 'np.log').replace('^', '**')
        y = eval(safe_func)
        
        fig = go.Figure()
        if plot_type == "Linear (خطي)":
            fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=func_str, line=dict(color='#00f2ff')))
        elif plot_type == "Polar (قطبي)":
            fig.add_trace(go.Scatterpolar(r=y, theta=x*18, mode='lines', name=func_str, line=dict(color='#7000ff')))
        
        fig.update_layout(template="plotly_dark", title=f"رسم الدالة: {func_str}")
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"خطأ في الرسم البياني: {e}")
