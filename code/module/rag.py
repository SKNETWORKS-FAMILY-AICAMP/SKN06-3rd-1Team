import os
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document


# Document 객체로 변환
def document_from_text(data, params) -> list[Document]:
    documents = []
    for policy_name, contents in data.items():
        merged_text = " ".join(contents)
        documents.append(
            Document(
                page_content=merged_text,
                metadata={"name": policy_name, "source": params["TOKENIZED_DATA_PATH"]},
            )
        )
    return documents


# 임베딩 모델 초기화
def embedding_model_init(params):
    embedding_model = OpenAIEmbeddings(model=params["EMBEDDING_MODEL_NAME"])
    return embedding_model


# Vector Store 생성/로드
def make_vector_store(documents, embedding_model, params):
    if os.path.exists(params["PERSIST_DIRECTORY"]):
        print(f"기존 Vector Store를 {params["PERSIST_DIRECTORY"]}에서 로드합니다.")
        vector_store = Chroma(
            persist_directory=params["PERSIST_DIRECTORY"],
            collection_name=params["COLLECTION_NAME"],
            embedding_function=embedding_model,
        )
    else:
        print(f"새로운 Vector Store를 {params["PERSIST_DIRECTORY"]}에 생성합니다.")
        os.makedirs(params["PERSIST_DIRECTORY"], exist_ok=True)
        vector_store = Chroma.from_documents(
            documents=documents,
            embedding=embedding_model,
            collection_name=params["COLLECTION_NAME"],
            persist_directory=params["PERSIST_DIRECTORY"],
        )
    return vector_store
