import streamlit as st
from utils import section_header, get_ai_explanation

def show():
    section_header("الكيمياء والكهرباء", "العلاقة بين المواد الكيميائية والتطبيقات الكهربائية")
    
    st.markdown("""
    <div class="rtl">
        هذا القسم مخصص لاستكشاف الخصائص الكيميائية للمواد المستخدمة في الهندسة الكهربائية، مثل الموصلات، أشباه الموصلات، والعوازل.
    </div>
    """, unsafe_allow_html=True)
    
    element = st.selectbox("اختر مادة/عنصر:", ["النحاس (Copper)", "السيليكون (Silicon)", "الألمنيوم (Aluminum)", "الجرمانيوم (Germanium)", "الليثيوم (Lithium)"])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"#### خصائص {element}")
        if "النحاس" in element:
            st.write("- الموصلية: عالية جداً")
            st.write("- الاستخدام: الأسلاك الكهربائية، المحركات")
        elif "السيليكون" in element:
            st.write("- الموصلية: شبه موصل")
            st.write("- الاستخدام: الترانزستورات، الخلايا الشمسية")
            
    with col2:
        if st.button(f"تحليل الذكاء الاصطناعي لـ {element}"):
            with st.spinner("جاري جلب البيانات..."):
                explanation = get_ai_explanation(f"Explain the chemical properties and electrical applications of {element}. Include conductivity and common uses in engineering.")
                st.info(explanation)
                
    st.divider()
    st.subheader("مقارنة المواد")
    mat1 = st.text_input("المادة الأولى:", "Copper")
    mat2 = st.text_input("المادة الثانية:", "Aluminum")
    
    if st.button("قارن باستخدام الذكاء الاصطناعي"):
        with st.spinner("جاري المقارنة..."):
            comparison = get_ai_explanation(f"Compare {mat1} and {mat2} in terms of electrical conductivity, cost, and engineering applications.")
            st.markdown(comparison)
