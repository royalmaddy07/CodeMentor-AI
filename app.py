# app.py file : is responsible for storing the application logic

# step 1. to load enviroument variables -> 
from dotenv import load_dotenv
from chatbot import llm
from prompts import programming_prompt
from chains import programming_chain

load_dotenv()

# step 3 : llm.invoke() function : used to ask the model
# this sends request via the internet to Google server -> Gemini -> sends back -> Response object
# object : is not a string, rather an AIMessage object with its own methods and properties

question = input("Topic: ")

response = programming_chain.invoke({ # using programming_chain/or any chain is part of "abstraction"
    "topic" : question
})
# we send a dictionary of key-value pairs which convert to variables and there values

print(response)
# we have changed response.content because we are using a string parser