from crewai import Agent
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma


# CrewAI Agent
retrieval_agent = Agent(
    role="Document Retrieval Specialist",

    goal="Retrieve relevant audit documents",

    backstory="Expert in enterprise document retrieval using vector databases",

    verbose=True
)


# RAG Retrieval Function
def retrieve_documents(query):

    embeddings = OpenAIEmbeddings()

    vectordb = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    retriever = vectordb.as_retriever(
        search_kwargs={"k": 5}
    )

    results = retriever.get_relevant_documents(query)

    return results