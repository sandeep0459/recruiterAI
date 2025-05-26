import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

#to load .env
load_dotenv()


#simple RAG pipeline
def ingest_documents():

    #loading text file (resume)
    loader = TextLoader("resume.txt")

    #convert it to langchain doc
    docs = loader.load()

    #chunking with logical fallback split rules
    splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100,
    separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = splitter.split_documents(docs)

    #embed each chunk into a vector using OpenAI 
    embeddings = OpenAIEmbeddings()

    #store the vector into a FAISS Index
    vectorstore = FAISS.from_documents(chunks,embeddings)

    #save the index locally
    vectorstore.save_local("vectorstore")


if __name__ == "__main__":
    ingest_documents()



