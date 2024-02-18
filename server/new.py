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
from langchain_openai import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

# environment api key
load_dotenv()

# accessing and reading pdf
def gist(pdf_name, read = "rb"):
    '''
    takes in the name of a pdf uploaded in frontend and returns four lists consisting of organized information
    '''
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    pdf_obj = open(pdf_name, read) # CHANGE THIS LATER
    pdf_reader = PyPDF2.PdfReader(pdf_obj)
    context = ''
    for i in range(len(pdf_reader.pages)):
        context += pdf_reader.pages[i].extract_text()

    # splits text extracted from pdf to chunks to make it more accurate
    splitter = CharacterTextSplitter(separator = '\n', chunk_size = 5000, chunk_overlap = 200, length_function = len)
    chunks = splitter.split_text(context)
    # verifying knowledge
    knowledge = FAISS.from_texts(chunks, embeddings)

    # ask the user for 3 prompts
    # loop through the 3 prompts and pass in the input for each value in the invoke 
    # generating ai prompted response
    input = ""
    formula_prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context

    <context>
    {context}
    </context>

    Question: {input}
    """)
    # formula_prompt = ChatPromptTemplate.from_template("Provide me with only a list of formulas used in this text and put it in latex. Present them in a comma separated list and nothing else")
    # definition_prompt = ChatPromptTemplate.from_template("Provide me with only a list of definitions used in this text. Present them in a comma separated list and nothing else")
    # key_idea_prompt = ChatPromptTemplate.from_template("Provide me with only a list of key ideas used in this text. Present them in a comma separated list and nothing else")

    # information chain - llm + retriever + document chain
    # large language model - chat open ai
    llm = ChatOpenAI(openai_api_key='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')

    document_chain = create_stuff_documents_chain(llm, formula_prompt)

    retriever = knowledge.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    # invoking response to input
    response = retrieval_chain.invoke({"input": "Output all the dates, definitions, examples and summary and use new lines and don't use :. Make sure the first entry of each category is the name of the corresponding category"})

    #print(response["answer"])

    ## Organizing the output into lists for the frontend
    #sections - key dates, definitions, examples, summary
    #words = ['Dates', '19th century', '1900', '1886', '', 'Definitions', 'Isotopes are atoms of the same element, which have different mass numbers.', 'Isobars are atoms having the same mass number but different atomic numbers.', 'Valency is the combining capacity of an atom.', '', 'Examples', 'Hydrogen/lithium/sodium atoms contain one electron each in their outermost shell, therefore each one of them can lose one electron. So, they are said to have valency of one.', 'Magnesium has two electrons in its outermost shell, therefore its valency is two.', 'Fluorine has 7 electrons in the outermost shell, and its valency is determined by subtracting seven electrons from the octet, giving it a valency of one.', '', 'Summary', '- Atoms consist of sub-atomic particles like protons and electrons.', '- Charged particles in matter are revealed through experiments involving static electricity.', '- Isotopes have the same atomic number but different mass numbers.', "- Thomson's model of the atom proposed electrons embedded in a positive sphere.", '- Valency is determined by the number of electrons in the outermost shell of an atom.']
    #['Isotopes are atoms of the same element, which have different mass numbers.', 'Isobars are atoms having the same mass number but different atomic numbers.', 'Valency is the combining capacity of an atom.']
    words = response["answer"].splitlines()
    summary_index = 0
    for i in range(len(words)):
        if (words[i] == 'Summary' or words[i] == 'summary'):
            summary_index = i
        elif ' ' in words[i]:
            if (words[i].split()[0] == 'Summary' or words[i].split()[0] == 'summary'):
                summary_index = i
    dates = words[1 : words.index('')-1]
    definitions = words[words.index('Definitions') + 1 : words.index('Examples')-1]
    examples = words[words.index('Examples') + 1 : summary_index-1]
    summary = words[summary_index + 1 : (len(words))]

    return dates, definitions, examples, summary



