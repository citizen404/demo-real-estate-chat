from langchain_openai import OpenAIEmbeddings
import numpy as np

class SimpleVectorStore:
    def __init__(self, docs):
        self.docs = docs
        self.embeddings = OpenAIEmbeddings()
        self.vectors = self.embeddings.embed_documents(docs)

    def search(self, query, k=3):
        query_vec = self.embeddings.embed_query(query)
        scores = np.dot(self.vectors, query_vec)
        top_k_idx = np.argsort(scores)[-k:][::-1]
        return [self.docs[i] for i in top_k_idx]
