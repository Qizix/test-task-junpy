from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFacePipeline


def get_llm():
    #

    return HuggingFacePipeline.from_model_id (
        model_id = "facebook/bart-large-cnn",
        task = "summarization",
        pipeline_kwargs = {
            "max_new_tokens": 100,
            "top_k": 50,
            "temperature": 0.1,
        }
    )

def get_prompt():
    template = """Write a concise summary of the following:
    "{text}"
    CONCISE SUMMARY:"""
    return PromptTemplate(template = template, input_variables = ["text"])

def summarize_text(text):
    llm = get_llm()
    prompt = get_prompt()
    llm_chain = LLMChain(llm = llm, prompt = prompt)
    result = llm_chain.invoke(text)
    print(result)
    return result['text']