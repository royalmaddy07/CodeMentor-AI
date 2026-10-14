# app.py file : is responsible for storing the application logic

# step 1. to load enviroument variables -> 
from dotenv import load_dotenv
load_dotenv()

from chatbot import llm
from prompts import programming_prompt
# from chains import conversation_chain

from graph import graph
from langchain_core.messages import HumanMessage


# step 3 : llm.invoke() function : used to ask the model
# this sends request via the internet to Google server -> Gemini -> sends back -> Response object
# object : is not a string, rather an AIMessage object with its own methods and properties

def main():
    config = {
        "configurable" : {
            "thread_id" : "user1"
        }
    }

    print("Welcome to AI Tutor!")
    print("Type 'exit' to quit.\n")

    while(True):
        question = input("You: ").strip()
        if question.lower() == "exit":
            break

        if not question:
            continue

        result = graph.invoke(
            {
                "messages": [
                    HumanMessage(content=question)
                ]
            },
            config=config
        )

        response = result["messages"][-1]

        print(f"\nAI Tutor: {response.content}\n")


if __name__ == "__main__":
    main()