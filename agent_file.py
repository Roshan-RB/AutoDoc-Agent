import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv

# Load your API key
load_dotenv()

# Initialize the AI model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

class State(TypedDict):
    code: str                # The code being analyzed
    language: str            # Programming language detected
    functionality: str       # What the code does
    documentation: str       # Generated documentation
    commented_code: str 

def detect_language(state: State):
    """Identify what programming language the code is written in"""
    
    prompt = PromptTemplate(
        input_variables=["code"],
        template="What programming language is the following code written in? Answer with just the language name.\n\nCode: {code}\n\nLanguage:"
    )

    chain = prompt | llm
    response = chain.invoke({"code": state["code"]})
    
    return {"language": response.content.strip()}


def analyze_functionality(state: State):
    """Determine what the code does and how it works"""
    
    prompt = PromptTemplate(
        input_variables=["code", "language"],
        template="Analyze this {language} code and explain what it does in 2-3 sentences. Focus on the main purpose and functionality.\n\nCode: {code}\n\nFunctionality:"
    )

    chain = prompt | llm
    response = chain.invoke({
        "code": state["code"],
        "language": state["language"]
    })
    
    return {"functionality": response.content.strip()}


def generate_documentation(state: State):
    """Create useful documentation for the code"""
    
    prompt = PromptTemplate(
        input_variables=["code", "language", "functionality"],
        template="""
        Based on this {language} code and its functionality, create documentation that includes:
        1. A brief description of what the code does
        2. Documentation for any functions (parameters, return values)
        3. Any potential improvements

        Code: {code}
        
        Functionality: {functionality}
        
        Documentation:
        """
    )
    
    chain = prompt | llm
    response = chain.invoke({
        "code": state["code"],
        "language": state["language"],
        "functionality": state["functionality"]
    })
    
    return {"documentation": response.content}

def insert_inline_comments(state: State):
    prompt = PromptTemplate(
        input_variables=["code", "language"],
        template="""
                    Insert concise inline comments into the following {language} code to explain each important line or block.

                    Code:
                    {code}

                    Commented Code:
                    """
    )
    chain = prompt | llm
    response = chain.invoke({
        "code": state["code"],
        "language": state["language"]
    })
    return {"commented_code": response.content.strip()}



# Create the workflow graph
workflow = StateGraph(State)

# Add our capabilities as nodes
workflow.add_node("detect_language", detect_language)
workflow.add_node("analyze_functionality", analyze_functionality)
workflow.add_node("generate_documentation", generate_documentation)
workflow.add_node("insert_inline_comments", insert_inline_comments)

# Set the workflow order
workflow.set_entry_point("detect_language")
workflow.add_edge("detect_language", "analyze_functionality")
workflow.add_edge("analyze_functionality", "generate_documentation")
workflow.add_edge("generate_documentation",  "insert_inline_comments")
workflow.add_edge("insert_inline_comments", END)

# Compile the agent
code_helper = workflow.compile()

# # Quick test
# response = llm.invoke("Can you hear me?")
# print(response.content)