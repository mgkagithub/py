import os
import openai
import pyttsx3 
import time 
openai.organization = "org-4R7gGAwRtsQb3FdDEG3fHVJ6"
openai.api_key = "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"

conversation = [{"role":"user","content": "you are a helpful assistant"}]

while(True):
    user_input = input("Prompt: ")
    conversation.append({"role":"user","content": user_input})

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = conversation
    )
    conversation.append({"role":"assistant","content": response['choices'][0]['messages']['content']})
    print("\n"+response['choices'][0]['messages']['content']+"\n")

