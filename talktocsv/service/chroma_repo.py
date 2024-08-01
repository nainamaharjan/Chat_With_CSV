"""
   Created by: Naina Maharjan
   Created on: 2024-08-01
"""
import chromadb

class ChromaRepo:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection("vetcors")

    def add_documents(self, documents, ids):
        self.collection.add(
            documents=documents,
            ids=ids)
        print("Added Embeddings")
        return True

    def search_vector(self, query, top_k):
        results = self.collection.query(
            query_texts=[query],
            n_results=top_k,
        )
        return results["documents"][0]


def get_chroma_client():
    return ChromaRepo()


