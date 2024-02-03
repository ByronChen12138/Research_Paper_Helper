import chainlit as cl
import openai

GPT4 = "gpt-4"
GPT3 = "gpt-3.5-turbo-0613"

# Open the file
file_path = 'OPENAI_API_KEY.txt'  # Replace with your OPENAI_API_KEY.txt.txt path
file = open(file_path, 'r')

# Read the contents
OPENAI_API_KEY = file.read()

# Close the file
file.close()

openai.api_key = OPENAI_API_KEY


# @cl.on_chat_start
# async def start():
#     await cl.Message(content="Feel free to ask me anything!").send()


@cl.on_chat_end
async def end():
    await cl.Message(content="See you in the future!").send()


@cl.on_message
async def main(msg: cl.Message):
    response = openai.ChatCompletion.create(
        model=GPT3,
        messages=[
            {"role": "system", "content": "You are a helpful assistant in a book store."},
            {"role": "user", "content": msg.content}
        ],
        temperature=1
    )

    await cl.Message(content=response["choices"][0]["message"]["content"]).send()
