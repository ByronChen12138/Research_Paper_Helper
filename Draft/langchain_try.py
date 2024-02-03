import os

import openai
import chainlit as cl
from langchain import PromptTemplate, OpenAI, LLMChain

template = """Question: {question}

Answer: Let's think step by step."""

# Open the file
file_path = './OPENAI_API_KEY.txt'  # Replace with your OPENAI_API_KEY.txt.txt path
file = open(file_path, 'r')

# Read the contents
OPENAI_API_KEY = file.read()

# Close the file
file.close()

openai.api_key = OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


@cl.on_chat_start
def main():
    prompt = PromptTemplate(
        template=template,
        input_variables=["question"]
    )

    llm_chain = LLMChain(
        prompt=prompt,
        llm=OpenAI(temperature=0, streaming=True),
        verbose=True
    )

    # Store it in the user session for latter usage
    cl.user_session.set("llm_chain", llm_chain)


@cl.on_message
async def main(message: cl.Message):
    llm_chain = cl.user_session.get("llm_chain")

    res = await llm_chain.acall(message.content, callbacks=[cl.AsyncLangchainCallbackHandler()])

    await cl.Message(content=res["text"]).send()
