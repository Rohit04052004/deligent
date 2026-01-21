import os
import chainlit as cl

from langchain.llms import Ollama
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import Pinecone as LangPinecone
from langchain.embeddings import PineconeEmbeddings

from pinecone import Pinecone

from dotenv import load_dotenv
load_dotenv()



# ---------------- PINECONE INIT ----------------

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index_name = os.getenv("PINECONE_INDEX_NAME")
index = pc.Index(index_name)

# ---------------- EMBEDDINGS (PINECONE HOSTED) ----------------

embeddings = PineconeEmbeddings(
    model="llama-text-embed-v2"
)

# ---------------- VECTOR STORE ----------------

vectorstore = LangPinecone(
    index=index,
    embedding=embeddings,
    text_key="text"
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# ---------------- LLM ----------------

llm = Ollama(model="llama3")

# ---------------- MEMORY ----------------

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# ---------------- RAG CHAIN ----------------

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory
)

# ---------------- LOAD DATA INTO PINECONE (ONLY FIRST TIME) ----------------

def upload_data():
    with open("data.txt", "r", encoding="utf-8") as f:
        text = f.read()

    chunks = [c.strip() for c in text.split("\n") if c.strip()]
    vectorstore.add_texts(chunks)

# ⚠️ Uncomment only FIRST TIME
# upload_data()

# ---------------- CHAINLIT UI ----------------

@cl.on_chat_start
async def start():
    await cl.Message(
        content="🤖 Jarvis Enterprise Assistant is online. Ask me about company knowledge."
    ).send()

@cl.on_message
async def main(message: cl.Message):
    query = message.content

    result = qa_chain.invoke({"question": query})
    answer = result["answer"]

    await cl.Message(content=answer).send()
