from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI    
from langchain.chains import RetrievalQA

#OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY")),

load_dotenv()

def get_qa_chain():

    #load stored resume chunks embedded as vectors
    vectorstore = FAISS.load_local(
    "vectorstore",
    OpenAIEmbeddings(),
    allow_dangerous_deserialization=True  
    )

    #create a retriever to fetch similar chunks related to query
    retriever = vectorstore.as_retriever()

    # Define the system prompt
    system_prompt = """
    You are Resume AI for Pranes Gopalan Venkatesh. When someone asks about 'yourself', 'you', or experience,
    always refer to "Pranes" in the third person. Do not pretend to be the user. Use factual information from the resume only.
    If a question is outside the scope of the resume (e.g., about personal opinions, politics, or unsupported claims), politely decline.
    Keep your tone formal, helpful, and concise.
    """

    prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_prompt),
    HumanMessagePromptTemplate.from_template("{context}\n\nQuestion: {question}")
    ])


    # Define LLM
    llm = ChatOpenAI(temperature=0.5, model_name="gpt-3.5-turbo")

    # Build QA chain with prompt injected
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt}
    )