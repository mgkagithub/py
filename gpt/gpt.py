import dotenv
from dotenv import load_dotenv
import openai
import os
dotenv.load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')
prompt = input("Enter a prompt:\n")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response["choices"][0]["text"])