from dotenv import load_dotenv
load_dotenv()

import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_restaurant_idea(cuisine):
    # Prompt 1: restaurant name
    prompt_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food. Suggest one fancy name."
    )

    name_chain = prompt_name | llm
    name_result = name_chain.invoke({"cuisine": cuisine})
    restaurant_name = name_result.content.strip()

    # Prompt 2: menu items
    prompt_menu = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest 5 menu items for a restaurant named {restaurant_name}. Give only names, comma separated."
    )

    menu_chain = prompt_menu | llm
    menu_result = menu_chain.invoke({"restaurant_name": restaurant_name})

    menu_items = [
        item.strip() for item in menu_result.content.split(",")
    ]

    return {
        "restaurant_name": restaurant_name,
        "menu_items": menu_items
    }