import dotenv
from dotenv import load_dotenv
import openai
import os
import pyttsx3
def talks(talk):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'english-us')
    engine.say(talk)
    engine.runAndWait()
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
  presence_penalty=0)
text = response["choices"][0]["text"]
print(text)
talks(text)