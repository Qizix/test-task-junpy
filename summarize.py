from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFacePipeline


def get_llm():
    # Import a simple summarization model from Hugging Face
    model =  HuggingFacePipeline.from_model_id (
        model_id = "facebook/bart-large-cnn",
        task = "summarization",
        pipeline_kwargs = {
            "max_new_tokens": 100,
            "top_k": 50,
            "temperature": 0.1,
        }
    )
    
    return model

def get_prompt():
    # Prompt settings
    template = """Write a concise summary of the following:
    "{text}"
    CONCISE SUMMARY:"""
    
    return PromptTemplate(template = template, input_variables = ["text"])

def summarize_text(text):
    # Get a language model (llm) and prompt 
    llm = get_llm()
    prompt = get_prompt()
    
    # Create chain and generate rezult summary
    llm_chain = LLMChain(llm = llm, prompt = prompt)
    result = llm_chain.invoke(text)
    
    return result['text']