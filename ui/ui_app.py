"""
   Created by: Naina Maharjan
   Created on: 2024-07-31
"""
import pandas as pd
import streamlit as st

from settings import API_KEY, CSV_FILE
from talktocsv.service.csv_data_pre_processor import convert_df_to_contextual_sentences
from talktocsv.service.cv_data_visualizer import visualize_cv
from talktocsv.service.talk_to_csv_service import TalkToCsv
from talktocsv.service.qa_agent import generate_response

print(API_KEY)
def query_kb(query,service):
    results = service.query_knowledge_base(query)
    response = generate_response(context="\n".join(results), query=query)
    return response


def main():
    dataframe = pd.read_csv(CSV_FILE)

    df = convert_df_to_contextual_sentences(dataframe, df_only=True)
    service = TalkToCsv(data_frame=dataframe)
    st.write("# Chat with Covid dataset")

    with st.expander("🔎 Dataframe Preview"):
        st.write(df.tail(10))

    if st.button("Calculate Embeddings"):
        st.info("Calculating Embeddings. Please wait. This will take some time.")
        finished = service.add_embeddings()
        if finished:
            st.info("Embeddings Added Successfully.")

    query_csv, visualize_csv = st.tabs(["Chat with CSV", "Visualize CSV"])
    with visualize_csv:
        query = st.text_area("Visualize Data")
        if st.button("Visualize"):
            response = visualize_cv(query, df, API_KEY)
            st.success(response)
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
            if response.endswith(".png"):
                st.image(response)
        with query_csv:
            query_text = st.text_area("Query:")
            if st.button("Submit"):
                if query_text:
                    response = query_kb(query_text, service)
                    st.info(response)
                else:
                    st.info("Empty input. Please type your query.")


if __name__ == '__main__':
    main()
