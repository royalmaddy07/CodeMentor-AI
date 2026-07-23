from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)

# note : {topic} -> placeholder managed by langchain, note that it only generates the prompt and does not invoke
# the brain/llm being used
programming_prompt = ChatPromptTemplate.from_messages([ # instead of .from_template()
    (
        "system",
        """
        You are an expert programming tutor.
        Explain concepts clearly.
        Use examples.
        Mention time complexity whenever applicable.
        """
    ),

    MessagesPlaceholder(# conversation history sits between the system message and the latest user query
        variable_name="history"
    ),

    (
        "human",
        "{topic}"
    )
]) # The instruction and the user input should not be mixed -> hence we are using a list of tuples
# this is useful because when we add chat history, system, human and AI messages are stored separately