## Art Gallery AI Chatbot

**IST 402 Group 12**
* *Owen Eller
* *Brielle Picard
* *Olive Ajilore
---

## Overview

The **Art Gallery AI Chatbot** is an intelligent conversational assistant designed to help users explore museum exhibitions, artists, and artworks. Built using **LangChain**, **OpenAI GPT models**, and a lightweight **Streamlit** interface, the chatbot simulates the experience of interacting with a knowledgeable gallery guide.

Users can ask questions such as:

* *“Tell me about Monet.”*
* *“What’s in the Modern Art exhibition?”*
* *“What is Impressionism?”*

The chatbot responds with short, accurate information sourced from a custom dataset and optimized prompt engineering.

---

## Features

* **Conversational AI** using GPT-3.5 Turbo
* **Custom prompt engineering** ensuring friendly, expert, 2–3 sentence responses
* **Streamlit Web UI** with chat history
* **Custom local API** (`gallery_api.py`) with curated artist & exhibition info
* **LangChain LLMChain** for predictable responses
* **Logging & error handling** for fault tolerance
* **Modular codebase** that can be easily extended

---

## Architecture

```text
User → Streamlit UI → LangChain LLMChain → Prompt Template → OpenAI GPT Model → Response
                          ↓
                  gallery_api.py (Artist & Exhibit Info)
```

Each component is modular, making it easy to expand with real museum APIs, databases, image models, or RAG pipelines.

---


## 🔧 Installation & Setup

### **1. Clone the Repository**

```bash
git clone https://github.com/YOUR_USERNAME/art-gallery-chatbot.git
cd art-gallery-chatbot
```

### **2. Create a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Add OpenAI API Key**

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

Your key will load automatically using `python-dotenv`.

---

## ▶️ Running the Application

Launch Streamlit:

```bash
streamlit run app.py
```

Open the UI in your browser:
[http://localhost:8501](http://localhost:8501)

---

## Usage

Once the app loads:

1. Type any question about artists, exhibitions, or artworks
2. The chatbot generates a concise, friendly answer
3. Chat history appears below the response
4. All interactions are logged in `chatbot.log`

---

## Prompt Engineering Design

The chatbot uses a structured LangChain prompt:

```
You are an expert art gallery assistant.  
Answer politely and provide interesting details about exhibitions, artists, or artworks.  
Keep the answer 2–3 sentences long.

User: {question}
Assistant:
```

This ensures:
Consistent tone
Factual responses
Controlled length
Avoidance of hallucination

---

## Integrations

### **Internal Dataset**

`gallery_api.py` provides curated details for:

* Monet
* Van Gogh
* Picasso
* Modern Art Exhibition
* Impressionism Exhibition
* Sculpture Hall

### **Language Model**

* OpenAI GPT-3.5 Turbo via LangChain `ChatOpenAI` wrapper
* Temperature set to `0.5` for balanced creativity & accuracy

---

## Error Handling & Logging

* If API key is missing → App stops and displays error
* Exceptions are caught and surfaced to UI
* `chatbot.log` records:

  * User questions
  * Model responses
  * Error traces

Example log entry:

```
2025-02-14 10:33:21 - INFO - User asked: Tell me about Monet.
2025-02-14 10:33:21 - INFO - Bot responded: Monet was a founder of Impressionism...
```

---

## Technologies Used

| Component   | Technology                            |
| ----------- | ------------------------------------- |
| LLM         | OpenAI GPT-3.5 Turbo                  |
| Framework   | LangChain (LLMChain, PromptTemplates) |
| Frontend    | Streamlit                             |
| Data Layer  | Python Dictionary API                 |
| Logging     | Python `logging` module               |
| Environment | `.env` with `python-dotenv`           |


