from langgraph.graph import MessagesState
from langgraph.graph import StateGraph
from langgraph.graph import START, END
from chatbot import llm

def chatbot(state: MessagesState):
    # here state -> variable name and : MessagesState -> TypeHint, ye bhi hota hai python me
    # the state is a dictionary which contains -> "messages" : [....] -> we extract that and give it to 
    # our llm/gemini
    # gemini returns us response = AIMessage object
    response = llm.invoke(state["messages"])
    # we update that to our state and return it
    return {
        "messages" : [response]
    }
    # we are returning this output, because langGraph knows that when a new 

graph_builder = StateGraph(MessagesState)
graph_builder.add_node("chatbot", chatbot)
# we told langgraph that there is a node whose name is chatbot & when you execute it, call the chatbot() function
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()# this creates/compiles our graph object

# important point to notice : response = chain.invoke() gave us the AIMessage or parsed string
# Now, result = graph.invoke() returns the state

# LangGraph is about running a workflow and updating the state
result = graph.invoke(
    {
        "messages" : [
            {
                "role" : "user",
                "content" : "what is binary search?"
            }
        ]
    }
)

print(result)