from chatbot import llm
from prompts import programming_prompt
from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables.history import RunnableWithMessageHistory
from memory import get_session_history

parser = StrOutputParser()

programming_chain = programming_prompt | llm
# we have removed StrOutputParser() from this chain
# why? because our Graph needs the AIMessage returned by gemini so that it can append that message to its
# conversation state
# the pipe symbol '|' is used to connect to 2 different components
# The output of the first automatically becomes the input of the second.

# conversation_chain = RunnableWithMessageHistory(
#     programming_chain, # parameter 1 : which chain should remember conversations

#     get_session_history, # how do I obtain the history?

#     input_messages_key="topic", 

#     history_messages_key="history"
# ) #