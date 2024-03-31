from langchain.prompts import PromptTemplate
from langchain.llms import OpenAIChat
from langchain.chains import LLMChain
import pandas as pd

# Step 1: Import the necessary modules
import os

# Step 2: Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = "PERSONAL API KEY"

# Step 4: Define the Prompt Template
prompt = PromptTemplate(
    input_variables=["abstract"],
    template="Is this paper a dataset paper? Paper abstract: {abstract}",
)


pubs_abstract = pd.read_csv("pubs_abstract_0.csv").reset_index()

for idx, row in pubs_abstract.iterrows():
    print(prompt.format(abstract=row['abstract']))

    llm = OpenAIChat(model_name='gpt-3.5-turbo-16k')
    chain = LLMChain(llm=llm, prompt=prompt)

    output = chain.run(row['abstract'])
    print(output)

    output = output.replace(',', '')
    output = output.replace('.', '')

    if 'yes ' in output.lower():
        dataset = True
    elif 'no ' in output.lower():
        dataset = False
    elif 'not ' in output.lower():
        dataset = False

    pubs_abstract.loc[idx, ["is_dataset"]] = dataset

pubs_abstract.to_csv("pubs_abstract_is_dataset.csv")
