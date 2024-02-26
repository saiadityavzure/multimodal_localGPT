from langchain.chains import StuffDocumentsChain, LLMChain, ConversationalRetrievalChain
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.vectorstores import Chroma 
import chromadb 
import yaml


with open("config.yml", "r") as f:
    config = yaml.safe_load(f)


def create_llm():
    pass


def create_llm_chain():
    pass


def create_chat_memory():
    pass



def create_prompt_from_template():
    pass


def load_normal_chain():
    pass


