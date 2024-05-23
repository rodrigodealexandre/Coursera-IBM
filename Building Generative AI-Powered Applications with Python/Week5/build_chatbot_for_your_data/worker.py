import os
import torch
from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.llms import HuggingFaceHub
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes, DecodingMethods
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models import Model

# Check for GPU availability and set the appropriate device for computation.
DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"

# Global variables
conversation_retrieval_chain = None
chat_history = []
llm_hub = None
embeddings = None

Watsonx_API = ""
Project_id= "skills-network"

# Function to initialize the language model and its embeddings
def init_llm():
    global llm_hub, embeddings
    
    params = {
        GenParams.MAX_NEW_TOKENS: 500, # The maximum number of tokens that the model can generate in a single run.
        GenParams.TEMPERATURE: 0.1,   # A parameter that controls the randomness of the token generation. A lower value makes the generation more deterministic, while a higher value introduces more randomness.
    }
    
    credentials = {
        'url': "https://us-south.ml.cloud.ibm.com",
    }
    
    LLAMA2_model = Model(
        model_id= 'meta-llama/llama-2-70b-chat',
        credentials=credentials,
        params=params,
        project_id=Project_id)

    llm_hub = WatsonxLLM(model=LLAMA2_model)

    # Initialize embeddings using a pre-trained model to represent the text data.
    # create object of Hugging Face Instruct Embeddings with (model_name,  model_kwargs={"device": DEVICE} )
    embeddings = HuggingFaceInstructEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={"device": DEVICE})

# Function to process a PDF document
def process_document(document_path):
    global conversation_retrieval_chain
    
    # Load the document
    loader =   PyPDFLoader(document_path) # ---> use PyPDFLoader and document_path from the function input parameter <---
    documents = loader.load()

    # Split the document into chunks, set chunk_size=1024, and chunk_overlap=64. assign it to variable text_splitter
    # ---> use Recursive Character TextSplitter and specify the input parameters <---
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1024,  # Maximum size of each chunk
        chunk_overlap=64  # Number of characters to overlap between chunks
    )
    texts = text_splitter.split_documents(documents)
    
    # Create an embeddings database using Chroma from the split text chunks.
    db = Chroma.from_documents(texts, embedding=embeddings)
    
    # Build the QA chain, which utilizes the LLM and retriever for answering questions.
    conversation_retrieval_chain = RetrievalQA.from_chain_type(
        llm=llm_hub,
        chain_type="stuff",
        retriever= db.as_retriever(search_type="mmr", search_kwargs={'k': 6, 'lambda_mult': 0.25}),
        return_source_documents=False
    )


# Function to process a user prompt
def process_prompt(prompt):
    global conversation_retrieval_chain
    global chat_history
    # Pass the prompt and the chat history to the conversation_retrieval_chain object
    output = conversation_retrieval_chain({"question": prompt, "chat_history": chat_history})
    
    answer =  output["result"]
    
    # Update the chat history
    # TODO: Append the prompt and the bot's response to the chat history using chat_history.append and pass `prompt` `answer` as arguments
    # --> write your code here <--	
    chat_history.append((prompt, answer))
    
    # Return the model's response
    return answer


# Initialize the language model
init_llm()
