"""
   Created by: Naina Maharjan
   Created on: 2024-07-28
"""
from talktocsv.service.csv_data_pre_processor import convert_df_to_contextual_sentences
from talktocsv.service.qa_agent import generate_response
from talktocsv.service.chroma_repo import get_chroma_client

class TalkToCsv:
    def __init__(self, data_frame):
        self.chroma_client = get_chroma_client()
        self.dataframe = data_frame

    def add_embeddings(self):
        contextual_sentences, ids, dataframe = convert_df_to_contextual_sentences(self.dataframe)
        print("Adding data to chroma db")
        self.chroma_client.add_documents(documents=contextual_sentences, ids=ids)
        self.dataframe = dataframe
        return True

    def query_knowledge_base(self, query):
        results = self.chroma_client.search_vector(query=query, top_k=30)
        print(results)
        response = generate_response(context="\n".join(results).strip(), query=query)
        return response





