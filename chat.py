import os
import openai
import streamlit as st

# Set your OpenAI API key
openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

def generate_response(input_text, chat_history):
    prompt = f"{chat_history}{restart_sequence}{input_text}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=None
    )
    reply = response.choices[0].text.strip()
    return reply

def chatbot_interface():
    global chat_history

    st.title("My Openai Chatbot")

    user_input = st.text_input("User Input")

    if st.button("Send"):
        reply = generate_response(user_input, chat_history)
        chat_history += f"{restart_sequence}{user_input}{start_sequence}{reply}"
        st.text_area("AI Response", value=reply, height=200)

if __name__ == "__main__":
    chat_history = ""
    chatbot_interface()
