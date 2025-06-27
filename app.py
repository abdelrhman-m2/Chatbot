import streamlit as st
import google.generativeai as genai
import time

# إعداد الصفحة
st.set_page_config(page_title="Gemini Chatbot 💬", page_icon="🤖")

# إعداد مفتاح Gemini API
GEN_API_KEY = "AIzaSyDw6MMR99ZxhvJhzEid412XPkl2ASUKy2o"
genai.configure(api_key=GEN_API_KEY)

# دالة للتفاعل مع Gemini
def chat_with_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")  # استخدم موديل مدعوم
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# عنوان الصفحة
st.title("🤖 Gemini AI Chatbot")
st.markdown("Ask about agriculture, AI, or anything else!")

# حفظ الرسائل داخل session
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# إدخال المستخدم
user_input = st.chat_input("💬 Type your question here...")

# معالجة الرد من Gemini
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # الحصول على رد Gemini
    response = chat_with_gemini(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})

    # عرض الرد بحركة كتابة
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        response_text = ""

        for char in response:
            response_text += char
            response_placeholder.markdown(response_text + "▌")
            time.sleep(0.003)

        response_placeholder.markdown(response_text)

#streamlit run chat.py