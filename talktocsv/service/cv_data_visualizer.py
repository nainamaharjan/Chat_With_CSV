"""
   Created by: Naina Maharjan
   Created on: 2024-07-31
"""

from pandasai.llm import OpenAI
from pandasai.smart_dataframe import SmartDataframe



def visualize_cv(query, df, api_key):
    llm = OpenAI(api_token=api_key)
    sdf = SmartDataframe(df, config={"llm":llm})
    response = sdf.chat(query)
    return response

