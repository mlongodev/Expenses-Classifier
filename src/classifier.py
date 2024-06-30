import openai
import json
from dotenv.main import load_dotenv
import os


def get_label(desc):
    try:
        load_dotenv();
        if 'PROMPT_CAT' in os.environ:
            prompt_cat_list = os.environ['PROMPT_CAT']
        else:
            # Default categories
            prompt_cat_list = "House rent, Supermarket, Internet home, Mobile phone, Gas, Electricity, Bank charges (card, taxes), Online services, Restaurants, Delivery, Aperitifs/bars, Shopping for Home, Clothes, Health, Courses, Technology, Transportation (plane, bus, subway, car)."

        if 'PROMPT_PRIVATE_INFO' in os.environ:
            prompt_private_info = os.environ['PROMPT_PRIVATE_INFO']
        else:
            prompt_private_info = ''

        content_system = ("I would like to classify my expenses using specific categories. In input you will have the list of categories and the description of an expense. Please associate a category to the expense. "
                        "Please only respond with the exact name of the category listed and nothing else. " 
                        + "Categories: \n") + prompt_cat_list + "\n" + prompt_private_info

        openai.organization = os.environ['OPENAI_ORG_ID']
        openai.api_key = os.environ['OPENAI_API_KEY']
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": content_system},
            {"role": "user", "content": "Expense description: " + str(desc)}]
        )
        data = completion.choices[0].message

        return data["content"]
    except Exception as e:
        # Handle the exception (e.g., log the error)
        print(f"An error occurred: {e}")
        return " "
    
def get_categories(chunk_data):
    try:
        load_dotenv();
        content_system = ('''You are an assistant who has the task of classifying my expenses using specific categories. In input you will have the list of categories and the description of an expense. Please associate a category to the expense. Please only respond with the exact name of the category listed and nothing else.\n 
                          Categories: House rent, Supermarket, Internet home, Mobile phone, Spotify, Netflix, Gas, Electricity, Bank charges (card, taxes), Other online services, Other (Fixed), Restaurants, Delivery, Aperitifs/bars, Shopping for Home, Clothes, Health, Courses, Technology, Transportation.
                          Other info: SI GUSTA is always Supermarket, dm drogerie is always Supermarket, laESSE is always Supermarket, CLESS TICKET ATM MILAN is always Transportation, Aspit Direz is always Transportation, SPOTIFY is always the Spotify category, Storytel is always Other online services category, Fastweb Spa is always Internet home, Martina Bregola in related with the House Rent category, Glovo is always Delivery, “A2a Spa Codice Mandato S9278668598” is always Electricity, “A2a Spa Codice Mandato S9231568484” is always Gas, Prime Video is always Other online services; Saf Srl is always Other.\n
                          Give me the response on a array Json. It should have the fields "id" with the id of the expense and "category" with the category for each expenses.''')

        openai.organization = os.environ['OPENAI_ORG_ID']
        openai.api_key = os.environ['OPENAI_API_KEY']
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": content_system},
            {"role": "user", "content": "Expenses description: " + str(chunk_data)}],
        response_format={ "type": "json_object" }
        )
        data = completion.choices[0].message
        print("NEW CALL")
        print(data)

        return data["content"]
    except Exception as e:
        # Handle the exception (e.g., log the error)
        print(f"An error occurred: {e}")
        return " "