import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

from rag.loader import load_properties, load_areas
from rag.retriever import SimpleVectorStore


load_dotenv()
client = OpenAI()

st.title("Real Estate AI Assistant")

# Load data once
@st.cache_resource
def init_store():
    props = load_properties("data/properties.csv")
    store = SimpleVectorStore(props)
    areas = load_areas("data/areas.txt")
    return store, areas

store, areas = init_store()

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask about properties")

if user_input:
    st.session_state.messages.append(("user", user_input))

    docs = store.search(user_input)
    context = "\n".join(docs)

    prompt = f"""
You are a professional real estate assistant.

Your behavior rules:

1. Do NOT ask all questions at once.
2. Ask only ONE clarifying question at a time.
3. Ask questions step by step like a real agent.

Required information:
- budget
- location
- bedrooms
- purpose (investment or living)

Process:
• If information is missing → ask ONE relevant question
• When most key information is known → suggest properties
• Explain briefly why they match
• Then ask if the client would like to schedule a viewing

Area info:
{areas}

Relevant properties:
{context}

Conversation history:
{st.session_state.messages}

Client question:
{user_input}

Respond professionally and concisely, like a real estate agent.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content

    st.session_state.messages.append(("assistant", answer))

for role, text in st.session_state.messages:
    st.chat_message(role).write(text)
