import torch
import os
import gradio as gr
#from langchain.llms import OpenAI
from langchain.llms import HuggingFaceHub
from transformers import pipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM
from ibm_watson_machine_learning.foundation_models.utils.enums import DecodingMethods
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models import Model

#######------------- LLM-------------####

# initiate LLM instance, this can be IBM WatsonX, huggingface, or OpenAI instance

llm = ###---> write your code here

#######------------- Prompt Template-------------####

# This template is structured based on LLAMA2. If you are using other LLMs, feel free to remove the tags
temp = """
<s><<SYS>>
List the key points with details from the context: 
[INST] The context : {context} [/INST] 
<</SYS>>
"""
# here is the simplified version of the prompt template
# temp = """
# List the key points with details from the context: 
# The context : {context} 
# """

pt = PromptTemplate(
    input_variables=["context"],
    template= temp)

prompt_to_LLAMA2 = LLMChain(llm=llm, prompt=pt)

#######------------- Speech2text-------------####

def transcript_audio(audio_file):
    # Initialize the speech recognition pipeline
    
    pipe = #------> write the code here
    
    # Transcribe the audio file and return the result
    transcript_txt = pipe(audio_file, batch_size=8)["text"]
    # run the chain to merge transcript text with the template and send it to the LLM
    result = prompt_to_LLAMA2.run(transcript_txt) 

    return result

#######------------- Gradio-------------####

audio_input = gr.Audio(sources="upload", type="filepath")
output_text = gr.Textbox()

# Create the Gradio interface with the function, inputs, and outputs
iface = #---> write code here

iface.launch(server_name="0.0.0.0", server_port=7860)