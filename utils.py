import pinecone
import openai
from config import *


openai.api_key = OPENAI_API_KEY
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def get_embedding(text):
    return client.embeddings.create(input=text, model=EMBEDDING_MODEL).data[0].embedding

def get_knowledge_text(knowledge_list):
    text = ""
    for data in knowledge_list:
        text += "<document>\n"
        for key, value in data.item():
            text += f"{key}: {value}\n"
        text += "</document>\n\n"
    return text