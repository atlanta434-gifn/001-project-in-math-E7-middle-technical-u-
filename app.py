import streamlit as st
import os

# Page configuration
st.set_page_config(
    page_title="الجامعة التقنية الوسطى - كلية البوليتكنك",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)
#ها علي شلونك
# 
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Cairo:wght@300;400;700&display=swap');
    
    :root {
        --primary-color: #00f2ff;
        --secondary-color: #7000ff;
        --bg-color: #0a0b1e;
        --text-color: #e0e0e0;
    }
    
    .main {
        background-color: var(--bg-color);
        color: var(--text-color);
        font-family: 'Cairo', sans-serif;
    }
    
    .stApp {
        background: radial-gradient(circle at 50% 50%, #1a1b3a 0%, #0a0b1e 100%);
    }
    
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif;
        color: var(--primary-color);
        text-shadow: 0 0 10px rgba(0, 242, 255, 0.5);
        text-align: center;
    }
    
    .header-container {
        padding: 2rem;
        border-bottom: 2px solid var(--primary-color);
        margin-bottom: 2rem;
        background: rgba(0, 242, 255, 0.05);
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.1);
    }
    
    .sidebar .sidebar-content {
        background-color: rgba(10, 11, 30, 0.9);
    }
    
    .stButton>button {
        background: linear-gradient(45deg, var(--secondary-color), var(--primary-color));
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 15px var(--primary-color);
    }
    
    .card {
        background: rgba(255, 255, 255, 0.05);
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid var(--primary-color);
        margin-bottom: 1rem;
    }
    
    /* RTL Support */
    .rtl {
        direction: rtl;
        text-align: right;
    }
    </style>
    """, unsafe_allow_html=True)

# اللهم صل على محمد وال محمد
st.markdown("""
    <div class="header-container rtl">
        <h1>الجامعة التقنية الوسطى - كلية البوليتكنك</h1>
        <h3>قسم تقنيات هندسة الالكترونيك والذكاء الاصطناعي</h3>
        <p style="text-align: center; font-size: 1.2rem; color: #7000ff;">
            إعداد الطلاب: حسن محمد جاسم - رؤى نديم كريم - علي نهاد قادر
        </p>
    </div>
    """, unsafe_allow_html=True)

# والله باردة
st.sidebar.image("photo_2026-02-04_23-53-08.jpg", use_container_width=True)

st.sidebar.markdown("""
    <div style="text-align: center; background: rgba(0, 29, 61, 0.5); padding: 10px; border-radius: 10px; border: 1px solid #00d4ff; margin-bottom: 10px;">
        <p style="color: #ffc300; font-weight: bold; margin-bottom: 5px; font-size: 1.1em;">إعداد الطلاب:</p>
        <p style="color: #ffffff; margin: 2px 0; font-size: 1em;">حسن محمد جاسم</p>
        <p style="color: #ffffff; margin: 2px 0; font-size: 1em;">رؤى نديم كريم</p>
        <p style="color: #ffffff; margin: 2px 0; font-size: 1em;">علي نهاد قادر</p>
    </div>
    """, unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.title("🚀 لوحة التحكم الهندسية")
st.sidebar.markdown("---")

sections = {
    "🏠 الصفحة الرئيسية": "home",
    "🔌 المنطق الرقمي": "digital_logic",
    "🧪 الكيمياء والكهرباء": "chemistry_electricity",
    "⚡ تحليل الدوائر (Kirchhoff)": "circuit_analysis",
    "📐 الجبر العام": "general_algebra",
    "📈 المجال والمدى": "domain_range",
    "📉 حساب التفاضل": "differential_calculus",
    "∫ حساب التكامل": "integral_calculus",
    "🧠 الجبر البولياني": "boolean_algebra",
    "🧩 المنطق الرياضي المتقدم": "advanced_math_logic",
    "⚛️ الحوسبة الكمية": "quantum_computing",
    "📟 الإلكترونيات وأشباه الموصلات": "electronics_semiconductors",
    "🔬 المختبر العملي DC-AC": "practical_lab",
    "📚 أساسيات الرياضيات والفيزياء": "basic_math_physics",
    "🏛️ فلسفة الرياضيات": "math_philosophy",
    "✍️ الرسم الهندسي (AutoCAD)": "autocad",
    "💡 أساسيات الكم والفوتونيات": "quantum_photonics",
    "🇬🇧 الإنجليزية للمهندسين": "english_for_engineers",
    "🌌 الفيزياء الكمية": "quantum_physics"
}

selection = st.sidebar.selectbox("اختر القسم:", list(sections.keys()))


if selection == "🏠 الصفحة الرئيسية":
    st.markdown("""
    <div class="rtl">
        <h2>مرحباً بكم في المنصة الهندسية المتكاملة</h2>
        <p>هذا التطبيق مصمم لتقديم تجربة تعليمية وتفاعلية متقدمة في مجالات الهندسة الإلكترونية والذكاء الاصطناعي.</p>
        <div class="card">
            <h4>✨ مميزات المنصة:</h4>
            <ul>
                <li>محاكاة تفاعلية للدوائر والمنطق الرقمي.</li>
                <li>حلول رياضية مدعومة بالذكاء الاصطناعي خطوة بخطوة.</li>
                <li>تمثيل بصري متقدم للبيانات والدوال.</li>
                <li>محتوى تعليمي شامل يغطي الفيزياء والكم واللغة الإنجليزية التقنية.</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    try:
        module_name = sections[selection]
        module = __import__(f"sections.{module_name}", fromlist=[module_name])
        module.show()
    except ImportError:
        st.error(f"عذراً، القسم المحدد ({selection}) غير متوفر حالياً.")
    except Exception as e:
        st.error(f"حدث خطأ أثناء تحميل القسم: {e}")

st.sidebar.markdown("---")
st.sidebar.info("شعبة E7")


