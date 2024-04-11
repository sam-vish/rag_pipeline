from langchain_anthropic import AnthropicLLM
from langchain_anthropic import ChatAnthropic
from langchain_community.document_loaders import TextLoader
import os
from dotenv import load_dotenv
load_dotenv()

geminiapikey = os.environ["GOOGLE_API_KEY"]
api_key = os.environ["ANTHROPIC_API_KEY"]

llm = ChatAnthropic(anthropic_api_key=api_key, model_name="claude-3-opus-20240229")

# Data Ingestion
loader=TextLoader("speech.txt")
text_documents=loader.load()
text_documents

from langchain_community.document_loaders import WebBaseLoader
import bs4

## load,chunk and index the content of the html page

loader=WebBaseLoader(web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
                     bs_kwargs=dict(parse_only=bs4.SoupStrainer(
                         class_=("post-title","post-content","post-header")

                     )))

text_documents=loader.load()