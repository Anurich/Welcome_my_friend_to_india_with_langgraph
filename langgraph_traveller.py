from typing import TypedDict, Annotated, Sequence, List
import operator
from langchain_core.messages import BaseMessage
import os
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import BaseTool, StructuredTool, tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser
from langgraph.prebuilt import ToolInvocation
import json
from langchain_core.messages import FunctionMessage
from langgraph.prebuilt import ToolExecutor

# agent state 
class AgentState(TypedDict):
    messages: List[str]
    history: List[str]
    last_visited_city: List[str]
    created_message: str
    print: bool = True



llm = ChatOpenAI()
duckduckgo_tool = DuckDuckGoSearchRun()


    


def common_tool(state):
    splitted = state.split("//")
    state, last_city = splitted[0], splitted[1]
    city_name = ""
    response = ""
    if state.lower() == "tired":
        # means need to sleep 
        response = "you have been traveling for long please take some rest"
    elif state.lower() =="hungary":
        location = input("Enter your location \t")
        prompt = "Please find top 5 highly rated restaurants near the location "+location
        response = duckduckgo_tool.invoke(prompt)

    elif state.lower()=="explore":
        location = input("Enter your location \t")
        prompt = f"Suggest top 5 places to visit near the {location} only gives the name of 5 places."
        response = duckduckgo_tool.invoke(prompt)
    
    elif state.lower() == "checkout":
        print(f"Thank you for visiting {last_city}, please visit again")
        input_question = input("Which city your going to! \t")
        prompt = """Please only return the name of the city from the query provided to you from the user {response}
        for example: 
        Input: I am visiting Agra
        output: Agra
        Input: Agra
        output: Agra
        """
        chain = PromptTemplate.from_template(prompt) | llm
        res = chain.invoke(input_question)
        city_name = res.content
        response = f"Welcome to {res.content}"
    

    elif state.lower() == "end_trip":
        response = """
            It's been an honor to host you in india, See you soon.
        """
        return response

    return {"messages": [response], "last_visited_city": [city_name]}


cm_tool = StructuredTool.from_function(
    func=common_tool,
    name="tool_for_multi_case",
    description="call this tool when ur \
                    1. Hungary: call this tool when someone express desired to eat something \
                    2. Tired: call this tool when someone is really tired and cannot perform any task \
                    3. Explore: when person is ready to move around and see new places \
                    4. Checkout: when someone wanted to leave the city or checkout from hotel \
                    5. end_trip: call this when the trip is finished or number of days for person to be in this country is over. \
                "
    )

tools = [cm_tool]
model = ChatOpenAI(temperature=0, streaming=True)
functions = [convert_to_openai_function(t) for t in tools]

Prompt = "Your an agent and you need to seprate some important keywords, for example if the person talk about the tiredness, you need \
     to create an argumen "
model = model.bind_functions(functions)

tool_executor = ToolExecutor(tools)


def agent(state):
    if not any(state["last_visited_city"]):
        entry_city = "new_delhi"
        state["last_visited_city"].append(entry_city)
        state["print"] = True
    else:
        entry_city = state["last_visited_city"][-1]
    if state["print"]:
        state["print"] =False
        print(f"Welcome to {entry_city} Enjoy your stay")
    state["messages"][-1].content = input("Enter the question \t")
    
    question = state["messages"][-1].content
    response = model.invoke(question)
    # history
    history = state["history"]
    history.append(response.content)

    return {"messages": [response], "history": history, "last_visited_city": state["last_visited_city"]}


def call_tools(state):

    last_message = state["messages"][-1]
    last_city = state["last_visited_city"][-1]
    
    parsed_tool_input = json.loads(last_message.additional_kwargs["function_call"]["arguments"])
    
    action = ToolInvocation(
        tool=last_message.additional_kwargs["function_call"]["name"],
        tool_input=parsed_tool_input['state']+"//"+last_city,
    )
    response = tool_executor.invoke(action)

    last_visited_city = response["last_visited_city"]
    if any(last_visited_city):
        state["last_visited_city"].extend(last_visited_city)
    
    function_message = FunctionMessage(content=str(response["messages"]), name=action.tool)

    history = state["history"]
    history.append(response["messages"][-1])
    
    return {"messages":[function_message], "history": history, "last_visited_city": state["last_visited_city"]}


def where_to_go(state):
    last_message = state["messages"][-1]
    
    if  json.loads(last_message.additional_kwargs["function_call"]["arguments"])["state"] == "end_trip":
        return "end"
    elif "function_call" in last_message.additional_kwargs:
        return "continue"
    else:
        return "main_agent"




from langgraph.graph import StateGraph, END
workflow = StateGraph(AgentState)

workflow.add_node("agent", agent)
workflow.add_node("call_tool", call_tools)

workflow.set_entry_point("agent")

workflow.add_conditional_edges("agent", where_to_go, {
    "continue": "call_tool",
    "main_agent": "agent",
    "end": END
})

workflow.add_edge("call_tool", "agent")
app = workflow.compile()

inputs = {"messages": [HumanMessage(content="")], "history": [], "last_visited_city": []}

for output in app.stream(inputs):
    # stream() yields dictionaries with output keyed by node name
    for key, value in output.items():
        if "call_tool" in key:
            print(f"Output from node '{key}':")
            print("---")        
            messages = value["messages"][0].content
            history = value["history"]
            last_visited_city = value["last_visited_city"]
            responses = json.dumps({
                "response": messages,
                "history": history,
                "visiting_city": last_visited_city
            }, indent=6)

            print(responses)
            with open("/Users/apple/Downloads/Traveling_to_india/ExploreWithAgents.json", "a") as fp:
                json.dump(json.loads(responses), fp, indent=6)


    print("\n---\n")

