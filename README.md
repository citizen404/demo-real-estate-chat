# Real Estate AI Assistant (Conversational RAG Demo)

A simple conversational AI assistant for real estate agencies.

This demo shows how AI can:

* respond to client inquiries instantly
* collect buyer requirements
* recommend suitable properties
* provide area insights
* qualify leads before an agent call

The assistant works like a **junior real estate agent available 24/7**.

---

## Features

**Client interaction**

* Natural conversation (ChatGPT-like interface)
* Step-by-step qualification:

  * Budget
  * Location
  * Bedrooms
  * Purpose (investment / living)

**Smart recommendations**

* Suggests relevant properties
* Explains why they match
* Includes area information
* Requests contact details for viewing

**Data sources**

* Property listings (CSV)
* Area descriptions
* Company knowledge (can be extended to PDFs, CRM, etc.)

---

## Demo Use Case

Example conversation:

> Client: I'm looking for investment property in Dubai
> Assistant: What budget range are you considering?
> Client: Around 1.5M
> Assistant: Which area are you interested in?
> ...
> Assistant: Based on your requirements, here are suitable options...

Business value:

* Instant response to new leads
* Reduced agent workload
* Pre-qualified clients
* Higher conversion rates

---

## Tech Stack

* Python
* Streamlit
* OpenAI API
* LangChain
* Simple vector search (embeddings-based)

Note: This is a lightweight demo designed for fast prototyping and client presentations.

---

## Project Structure

```
real-estate-demo/
│
├── app.py                 # Streamlit application
├── data/
│   ├── properties.csv     # Sample property data
│   └── areas.txt          # Area information
├── rag/
│   ├── loader.py          # Data loading
│   └── retriever.py       # Simple vector search
├── requirements.txt
└── .env                   # OpenAI API key
```

---

## Installation

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/real-estate-demo.git
cd real-estate-demo
```

### 2. Create virtual environment (recommended)

```
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add OpenAI API key

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## Run the Demo

```
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## Customization

This demo can be easily adapted for real projects:

* Replace `properties.csv` with real listings
* Add project brochures (PDF → embeddings)
* Connect to CRM
* Integrate WhatsApp / website chat
* Deploy to cloud

Typical MVP implementation time: **2–4 weeks**

---

## Disclaimer

This project is a demonstration prototype intended for client presentations and concept validation.

---

## Author

AI Automation & Business Process Solutions
Available for real estate AI implementations and custom automation projects.