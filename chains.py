from chatbot import llm
from prompts import programming_prompt
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

programming_chain = programming_prompt | llm | parser
# the pipe symbol '|' is used to connect to 2 different components
# The output of the first automatically becomes the input of the second.