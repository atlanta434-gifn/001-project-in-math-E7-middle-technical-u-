import streamlit as st
import pandas as pd
from utils import section_header, get_ai_explanation

def show():
    section_header("المنطق الرقمي", "محاكاة البوابات المنطقية وجداول الحقيقة")
    
    tab1, tab2, tab3 = st.tabs(["بوابات منطقية فردية", "محاكاة SOP/POS", "تحويل الأنظمة العددية"])
    
    with tab1:
        st.subheader("محاكاة البوابات")
        gate_type = st.selectbox("اختر البوابة:", ["AND", "OR", "NOT", "NAND", "NOR", "XOR", "XNOR"])
        
        col1, col2 = st.columns(2)
        with col1:
            in1 = st.checkbox("Input A", value=False)
            if gate_type != "NOT":
                in2 = st.checkbox("Input B", value=False)
        
        # Logic Calculation
        result = False
        if gate_type == "AND": result = in1 and in2
        elif gate_type == "OR": result = in1 or in2
        elif gate_type == "NOT": result = not in1
        elif gate_type == "NAND": result = not (in1 and in2)
        elif gate_type == "NOR": result = not (in1 or in2)
        elif gate_type == "XOR": result = in1 != in2
        elif gate_type == "XNOR": result = in1 == in2
        
        with col2:
            st.metric("النتيجة (Output)", "1" if result else "0")
            
        # Truth Table
        st.markdown("#### جدول الحقيقة (Truth Table)")
        if gate_type != "NOT":
            data = {
                "A": [0, 0, 1, 1],
                "B": [0, 1, 0, 1],
                "Output": [0, 0, 0, 1] if gate_type == "AND" else 
                          [0, 1, 1, 1] if gate_type == "OR" else
                          [1, 1, 1, 0] if gate_type == "NAND" else
                          [1, 0, 0, 0] if gate_type == "NOR" else
                          [0, 1, 1, 0] if gate_type == "XOR" else
                          [1, 0, 0, 1]
            }
        else:
            data = {"A": [0, 1], "Output": [1, 0]}
        
        st.table(pd.DataFrame(data))
        
        if st.button("شرح الذكاء الاصطناعي لهذه البوابة"):
            with st.spinner("جاري التفكير..."):
                explanation = get_ai_explanation(f"Explain the {gate_type} logic gate and its truth table.")
                st.info(explanation)

    with tab2:
        st.subheader("SOP & POS Forms")
        st.write("أدخل التعبير المنطقي للحصول على التبسيط والشرح:")
        expression = st.text_input("التعبير (مثال: A'B + AB'):", "A'B + AB'")
        if st.button("تحليل التعبير"):
            with st.spinner("جاري التحليل..."):
                explanation = get_ai_explanation(f"Analyze and simplify the boolean expression: {expression}. Explain SOP and POS forms.")
                st.markdown(explanation)

    with tab3:
        st.subheader("تحويل الأنظمة العددية")
        num_input = st.text_input("أدخل القيمة:", "10")
        from_base = st.selectbox("من نظام:", ["Decimal", "Binary", "Hexadecimal"])
        
        try:
            if from_base == "Decimal": val = int(num_input)
            elif from_base == "Binary": val = int(num_input, 2)
            else: val = int(num_input, 16)
            
            st.write(f"**العشري:** {val}")
            st.write(f"**الثنائي:** {bin(val)[2:]}")
            st.write(f"**الست عشري:** {hex(val)[2:].upper()}")
        except ValueError:
            st.error("يرجى إدخال قيمة صحيحة للنظام المختار.")
