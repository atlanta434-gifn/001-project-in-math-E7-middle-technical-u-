import streamlit as st
from openai import OpenAI
import random

def get_ai_explanation(prompt, context="", provider=None):
    # 1. قائمة بمفاتيحك الأربعة
    api_keys = [
        st.secrets.get("GROQ_API_KEY_1"),
        st.secrets.get("GROQ_API_KEY_2"),
        st.secrets.get("GROQ_API_KEY_3"),
        st.secrets.get("GROQ_API_KEY_4")
    ]
    
    # تصفية المفاتيح الموجودة فعلياً فقط
    valid_keys = [k for k in api_keys if k]
    
    if not valid_keys:
        return "خطأ: لم يتم العثور على مفاتيح API في Secrets."

    # 2. تحديد الموديل المطلوب (استخدام الأقوى افتراضياً)
    # يمكنك تغيير الموديل هنا لجميع الأقسام الـ 18 بضغطة واحدة
    selected_model = "llama-3.3-70b-versatile" 
    
    # 3. محاولة الاتصال مع نظام حماية (Try-Except)
    random.shuffle(valid_keys) # خلط المفاتيح لتوزيع الحمل بالتساوي
    
    for key in valid_keys:
        try:
            client = OpenAI(api_key=key, base_url="https://api.groq.com/openai/v1")
            
            full_prompt = f"Context: {context}\n\nUser Question: {prompt}\n\nPlease provide a detailed, step-by-step engineering explanation in Arabic."
            
            response = client.chat.completions.create(
                model=selected_model,
                messages=[
                    {"role": "system", "content": "أنت بروفيسور هندسي خبير، تشرح المفاهيم بوضوح تام وباللغة العربية العلمية."},
                    {"role": "user", "content": full_prompt}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content
            
        except Exception as e:
            # إذا فشل مفتاح (مثلاً وصل للحد الأقصى)، سينتقل المفتاح التالي في الحلقة
            continue 
            
    return "عذراً، جميع مفاتيح الخدمة مشغولة حالياً. يرجى المحاولة بعد دقيقة."

def section_header(title, subtitle=""):
    st.markdown(f"""
    <div style="direction: rtl; text-align: right; border-right: 5px solid #00f2ff; padding-right: 15px; margin-bottom: 20px;">
        <h2 style="color: white; margin-bottom: 5px;">{title}</h2>
        <p style="color: #00f2ff; font-size: 1.1em;">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)
