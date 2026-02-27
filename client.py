import requests
import streamlit as st
import speech_recognition as sr

st.title('Langchain Demo with LLAMA2 And Google GEMMA API')


def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
                             json={'input': {'topic': input_text}})
    return response.json()['output']['content']

def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
                             json={'input': {'topic': input_text}})
    return response.json()['output']

#Voice Recognition Feature Addition
def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Speak now")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        st.success(f"You said: {text}")
        return text
    except Exception as e:
        st.error(f"Could not recognize speech: {e}")
        return ""

input_text = st.text_input("Write an Essay on (Text Input)")
if st.button("Speak Topic for Essay"):
    voice_input = get_voice_input()
    if voice_input:
        st.write(get_openai_response(voice_input))

if input_text:
    st.write(get_openai_response(input_text))

#User Input
input_text1 = st.text_input("Write a Poem on (Text Input)")
if st.button("Speak Topic for Poem"):
    voice_input1 = get_voice_input()
    if voice_input1:
        st.write(get_ollama_response(voice_input1))

if input_text1:
    st.write(get_ollama_response(input_text1))
