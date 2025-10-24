import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.openrouter import OpenRouter
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb


# load environment variables from .env file
load_dotenv()

api_key = os.getenv("Open_router_API_Key")

documents = SimpleDirectoryReader('data').load_data()

chroma_client = chromadb.PersistentClient(path="./chroma_db")
