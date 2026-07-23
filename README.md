# 🧠 CodeMentor AI

An intelligent, conversational **programming tutor** powered by **Google Gemini 2.5 Flash** and built with the **LangChain** framework. CodeMentor AI explains programming concepts clearly, remembers conversation context across turns, and delivers a seamless learning experience — all from the terminal.

---

## ✨ Features

- **Expert Programming Tutoring** — Get clear, structured explanations of any programming concept.
- **Conversational Memory** — The chatbot remembers previous messages within a session, enabling natural follow-up questions.
- **Session Management** — Supports independent conversation histories per user via session IDs.
- **Modular Architecture** — Clean separation of concerns across dedicated modules (LLM, prompts, chains, memory).
- **LangChain LCEL Pipelines** — Uses LangChain Expression Language for composable, maintainable chains.
- **Easily Extensible** — Swap the LLM provider, add new prompt templates, or plug in a persistent memory backend — all without restructuring the app.

---

## 🏗️ Architecture

```
User Input
    │
    ▼
┌──────────────────────────────────────────────────┐
│              Conversation Chain                  │
│  ┌────────────┐  ┌─────────┐  ┌──────────────┐  │
│  │   Prompt    │→│   LLM   │→│ Output Parser │  │
│  │  Template   │  │ (Gemini)│  │  (StrOutput)  │  │
│  └────────────┘  └─────────┘  └──────────────┘  │
│         ▲                                        │
│         │                                        │
│  ┌──────────────────────┐                        │
│  │  Message History     │                        │
│  │  (In-Memory Store)   │                        │
│  └──────────────────────┘                        │
└──────────────────────────────────────────────────┘
    │
    ▼
  Response
```

The pipeline follows the LangChain Expression Language (LCEL) pattern:

```
Variables → Prompt Template → LLM → Output Parser → Response
```

Conversation history is automatically injected, stored, and updated by `RunnableWithMessageHistory`.

---

## 📁 Project Structure

```
CodeMentor-AI/
│
├── app.py              # Application entry point and main interaction loop
├── chatbot.py          # LLM configuration (Google Gemini 2.5 Flash)
├── prompts.py          # Prompt templates with system instructions
├── chains.py           # LCEL chain definitions and conversation chain setup
├── memory.py           # Session-based conversation history management
│
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

| Module | Responsibility |
|---|---|
| `app.py` | Runs the interactive loop; takes user input and displays responses |
| `chatbot.py` | Initializes the LLM (Gemini 2.5 Flash) with configuration |
| `prompts.py` | Defines reusable `ChatPromptTemplate` with system and human messages |
| `chains.py` | Connects prompt → LLM → parser via LCEL; wraps with message history |
| `memory.py` | Provides in-memory chat history storage and retrieval per session |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+**
- A **Google AI API Key** ([Get one here](https://aistudio.google.com/apikey))

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/royalmaddy07/CodeMentor-AI.git
   cd CodeMentor-AI
   ```

2. **Create and activate a virtual environment**

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS / Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   ```bash
   # Copy the example file
   cp .env.example .env
   ```

   Open `.env` and replace the placeholder with your actual API key:

   ```env
   GOOGLE_API_KEY = "your-google-api-key-here"
   ```

### Usage

```bash
python app.py
```

Start typing programming topics or questions, and CodeMentor AI will provide detailed explanations:

```
Topic: Binary Search
Binary Search is a highly efficient searching algorithm that works on sorted arrays...

Topic: What is its time complexity?
As I mentioned, Binary Search has a time complexity of O(log n)...
```

> 💡 The chatbot remembers your previous messages within the session, so you can ask follow-up questions naturally.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| [LangChain](https://www.langchain.com/) | Framework for building LLM-powered applications |
| [Google Gemini 2.5 Flash](https://deepmind.google/technologies/gemini/) | Large Language Model for generating responses |
| [LangChain LCEL](https://python.langchain.com/docs/concepts/lcel/) | Expression language for composing chains |
| [Python-dotenv](https://pypi.org/project/python-dotenv/) | Secure environment variable management |

---

## 🔧 Configuration

### Switching the LLM

To use a different model, update [chatbot.py](chatbot.py):

```python
# Example: Switch to a different Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    temperature=0.7  # Higher = more creative responses
)
```

### Adding New Prompt Templates

Create new templates in [prompts.py](prompts.py) for different tutoring personas:

```python
math_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert mathematics tutor. Explain concepts step by step."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{topic}")
])
```

### Persistent Memory

The current implementation uses in-memory storage. To persist conversations, replace the memory backend in [memory.py](memory.py) with:

- **Redis** — For fast, distributed session storage
- **PostgreSQL** — For durable, queryable conversation logs
- **MongoDB** — For flexible document-based storage

The modular design means no changes are needed in the chain or application logic.

---

## 🗺️ Roadmap

- [ ] Add a web-based UI (Streamlit / Gradio)
- [ ] Implement persistent memory with Redis or PostgreSQL
- [ ] Support multiple tutor personas (Math, Science, Interview Coach)
- [ ] Add RAG (Retrieval-Augmented Generation) for documentation-aware tutoring
- [ ] Implement token-aware memory strategies (sliding window, summarization)
- [ ] Add streaming responses for real-time output

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 📬 Contact

**Yash Patel** — [@royalmaddy07](https://github.com/royalmaddy07)

Project Link: [https://github.com/royalmaddy07/CodeMentor-AI](https://github.com/royalmaddy07/CodeMentor-AI)

---

<p align="center">
  Built with ❤️ using LangChain & Google Gemini
</p>
