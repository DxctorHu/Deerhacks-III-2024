import os
import openai
import PyPDF2
import re


from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import OpenAI


load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

pdf_obj = open("sample_pdf.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(pdf_obj)
text = ''
for i in pdf_reader.pages:
    text += i.extract_text()

splitter = CharacterTextSplitter(separator = '\n', chunk_size = 1000, chunk_overlap = 200, length_function = len)
chunks = splitter.split_text(text)
knowledge = FAISS.from_texts(chunks, embeddings)

formula_prompt = ChatPromptTemplate.from_template("Provide me with only a list of formulas used in this text and put it in latex. Present them in a comma separated list and nothing else")
definition_prompt = ChatPromptTemplate.from_template("Provide me with only a list of definitions used in this text. Present them in a comma separated list and nothing else")
key_idea_prompt = ChatPromptTemplate.from_template("Provide me with only a list of key ideas used in this text. Present them in a comma separated list and nothing else")


# pass in the PDF into the model and provide it with 3 prompts
# have the PDF return the data as one string
# Format the returned data into a list, separated by commas

llm = ChatOpenAI(openai_api_key="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")


# llm_chain = formula_prompt | llm


#chain = RetrievalQA.fromLLM(client, chain_type="stuff")
# formula_response = chain.run(input_documents=knowledge, question=formula_prompt)
# formula_response = llm_chain.invoke(knowledge, formula_prompt)
# formula_response = llm.invoke("")

#converting prompt data to list\
# definition_list =  re.split(', |,|\s,', definition_prompt)
# key_idea_list = re.split(', |,|\s,', key_idea_prompt)
# formula_list = re.split(', |,|\s,', formula_response)


heading = ''

