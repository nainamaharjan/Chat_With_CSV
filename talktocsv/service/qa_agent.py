"""
   Created by: Naina Maharjan
   Created on: 2024-07-28
"""

from settings import LLM_MODEL_NAME, API_KEY
from guidance import models, system, assistant, gen

QA_PROMPT = """
#System
You will be provided with multiple data of  patients of covid. Your job is to analyze the data given to you and 
reply to the user's query based on your analysis of the data given in the context.

#Covid Patient Data

{{context}}

User Query: 
{{question}}
"""


def generate_response(context, query):
    gpt = models.OpenAI(model=LLM_MODEL_NAME, api_key=API_KEY)
    with system():
        lm = gpt + QA_PROMPT.replace("{{context}}", context).replace("{{question}}", query)
    with assistant():
        lm += gen("response")
    return lm["response"]