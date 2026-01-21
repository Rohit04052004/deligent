# 🤖 Diligent — Enterprise AI Assistant (Jarvis)

## Overview
Diligent (Jarvis) is an enterprise-style conversational AI assistant built using LLaMA (self-hosted via Ollama), Pinecone Vector Database, and Chainlit UI.
It uses Retrieval Augmented Generation (RAG) with conversation memory to answer user queries based on internal documents such as company policies, guidelines, or project notes.

This project demonstrates how real-world GenAI systems are built for enterprise use cases and is designed for placement and interview demonstrations.

## Features
- 📚 Document-based Question Answering using RAG
- 🧠 Conversation Memory (multi-turn contextual chat)
- ☁️ Pinecone Cloud Vector Database for semantic search
- 🦙 Self-hosted LLaMA 3 using Ollama
- 💬 Real-time Chat UI using Chainlit
- 🔐 Secure API key handling using .env file
- ⚡ Fast semantic retrieval and accurate responses

## Requirements
- Python 3.10 or higher (recommended: 3.11)
- Ollama installed (for local LLaMA model)
- Pinecone account and API key
- Stable internet connection (for Pinecone)

## Installation

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd deligent
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install chainlit langchain pinecone-client python-dotenv ollama pypdf
```

### Step 5: Install Ollama and Model
Download Ollama from: https://ollama.com/download

```bash
ollama pull llama3
```

## Configuration

### Environment Variables
Create a `.env` file in the project root directory:

```bash
PINECONE_API_KEY=your_api_key_here
PINECONE_INDEX_NAME=jarvis
```

⚠️ Do not upload `.env` to GitHub.

Add the following to `.gitignore`:

```bash
.env
venv/
__pycache__/
```

## Usage

### Step 1: Add Knowledge Base
Edit `data.txt` and add your documents:

```
Leave Policy:
Employees get 12 casual leaves per year.

WFH Policy:
Employees can work from home twice a month.
```

### Step 2: Upload Data to Pinecone (First Time Only)
In `app.py`, uncomment:

```python
upload_data()
```

Run once:

```bash
chainlit run app.py
```

After data is uploaded, comment the line again to avoid duplicate vectors.

### Step 3: Run the Application
```bash
chainlit run app.py
```

Open the browser and start chatting with Jarvis.

### Example Queries
- How many leaves are allowed?
- Can I work from home?
- Can I take both in the same month?

Jarvis will respond using document knowledge and conversation context.

## Project Structure
```
deligent/
├── app.py              # Main Chainlit + RAG application
├── data.txt            # Knowledge base
├── .env                # Environment variables (ignored)
├── .gitignore
├── requirements.txt    # Optional dependency list
├── venv/               # Virtual environment (ignored)
└── README.md
```

## System Architecture
User → Chainlit UI → Retriever (Pinecone Vector DB) →  
Relevant Chunks + Chat History → LLaMA (Ollama) → Final Answer

This architecture minimizes hallucinations and ensures accurate responses based on documents.

## Use Cases
- 🏢 Company HR policy assistant
- 🎓 College administration chatbot
- 📄 Project documentation assistant
- 🤝 Internal team knowledge assistant

## Future Enhancements
- 📤 PDF upload from Chainlit UI
- 🔐 User authentication
- 🧠 Long-term memory with database storage
- 🌐 FastAPI backend integration
- 📊 Chat analytics and logging

## Contributing
1. Fork the repository
2. Create your feature branch
   ```bash
   git checkout -b feature/NewFeature
   ```
3. Commit your changes
   ```bash
   git commit -m "Add NewFeature"
   ```
4. Push to the branch
   ```bash
   git push origin feature/NewFeature
   ```
5. Open a Pull Request

## Troubleshooting

### Common Issues
- **Ollama not running**  
  → Start Ollama and verify using:
  ```bash
  ollama list
  ```
- **Pinecone authentication error**  
  → Check `.env` file and restart terminal.
- **Bot not answering correctly**  
  → Ensure documents were uploaded to Pinecone.

## License
This project is released under the MIT License.

## Author
Rohit Chigatapu  
B.Tech CSE (AI/ML) | GenAI Developer | Computer Vision Enthusiast

## Acknowledgments
- LangChain
- Pinecone
- Chainlit
- Ollama (LLaMA Models)

## Changelog

### Version 1.0.0
- Chainlit UI chatbot
- Pinecone vector database integration
- RAG pipeline
- Conversation memory
- Secure API handling using .env

**Last Updated**: January 21, 2026
