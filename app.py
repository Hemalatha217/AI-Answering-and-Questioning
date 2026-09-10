import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="AI Question Answering Chatbot",
    page_icon="🤖",
    layout="centered"
)

@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="Qwen/Qwen2.5-0.5B-Instruct"
    )

chatbot = load_model()

st.markdown("""
<style>
.stApp{
    background: linear-gradient(135deg,#667eea,#764ba2);
}

.title{
    text-align:center;
    color:white;
    font-size:42px;
    font-weight:bold;
}

.answer-box{
    background:white;
    padding:20px;
    border-radius:12px;
    color:black;
    margin-top:20px;
}

.stButton > button{
    width:100%;
    height:50px;
    border-radius:10px;
    font-size:18px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<p class="title">🤖 AI Question Answering Chatbot</p>',
    unsafe_allow_html=True
)

question = st.text_area(
    "Ask Your Question",
    placeholder="What is Artificial Intelligence?"
)

col1, col2 = st.columns(2)

with col1:
    ask = st.button("🚀 Ask AI")

with col2:
    clear = st.button("🗑️ Clear")

if clear:
    st.rerun()

if ask:

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Generating Answer..."):

            messages = [
                {"role": "user", "content": question}
            ]

            result = chatbot(
                messages,
                max_new_tokens=150,
                do_sample=False
            )

            answer = result[0]["generated_text"][-1]["content"]

            st.markdown(
                f"""
                <div class="answer-box">
                    <h3>🤖 AI Answer</h3>
                    <p>{answer}</p>
                </div>
                """,
                unsafe_allow_html=True
            )