import os
import openai
import PyPDF2
import re


from langchain.chains import LLMChain
from dotenv import load_dotenv
# from langchain.llms import OpenAI
from langchain_community.llms import OpenAI
#from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import OpenAI

load_dotenv()

# client = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY)\\
# OPEN_API_KEY = os.getenv("OPEN_API_KEY")

# print(OPEN_API_KEY)
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

llm = OpenAI(openai_api_key="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")
pdf_obj = open("sample_pdf.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(pdf_obj)
text = ''
for i in pdf_reader.pages:
    text += i.extract_text()

splitter = CharacterTextSplitter(separator = '\n', chunk_size = 1000, chunk_overlap = 200, length_function = len)
chunks = splitter.split_text(text)
knowledge = FAISS.from_texts(chunks, embeddings)

formula_prompt = ChatPromptTemplate.from_template("a list of formulas used in this text. Present them in a comma separated list and nothing else")
definition_prompt = ChatPromptTemplate.from_template("a list of definitions used in this text. Present them in a comma separated list and nothing else")
key_idea_prompt = ChatPromptTemplate.from_template("a list of key ideas used in this text. Present them in a comma separated list and nothing else")


#prompt = "N/A" # change this later to instructions

llm_chain = formula_prompt | llm

#chain = RetrievalQA.fromLLM(client, chain_type="stuff")
# formula_response = chain.run(input_documents=knowledge, question=formula_prompt)
# formula_response = llm_chain.invoke(knowledge, formula_prompt)
formula_response = llm_chain.invoke(knowledge)

#converting prompt data to list
definition_list =  re.split(', |,|\s,', definition_prompt)
key_idea_list = re.split(', |,|\s,', key_idea_prompt)
formula_list = re.split(', |,|\s,', formula_response)


heading = ''

