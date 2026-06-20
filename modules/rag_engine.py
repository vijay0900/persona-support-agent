from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os


def create_vector_database():

    documents=[]

    folder="docs"

    for file in os.listdir(folder):

        if file.endswith(".txt"):

            loader=TextLoader(
                os.path.join(folder,file)
            )

            documents.extend(
                loader.load()
            )

    splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs=splitter.split_documents(
        documents
    )

    embeddings=HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db=FAISS.from_documents(
        docs,
        embeddings
    )

    db.save_local(
        "vector_store"
    )

    print(
        "Vector database created successfully!"
    )