from langchain_core.chat_history import InMemoryChatMessageHistory
# why InMemory? because it lives in the RAM, the conversation is erased when we close the program
# later we can replace this with 1.Redis 2.PostgreSQL 3.MongoDB without changing our chain

# step 1 : create one history
history = InMemoryChatMessageHistory()

# step 2 : create one function
def get_session_history(session_id):
    # why not without session_id? This design allows one application to support many independent users.
    # each user will have its own chat history, which is identified using session_id
    return history