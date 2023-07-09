import openai
from dotenv.main import load_dotenv
import os


def get_label(desc):
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

    content_system = ("I would like to classify my expenses using specific categories. In input you will have the list of categories and the description of a expense. Please associate a category to the expense. "
                      "Please only respond with the exact name of the category listed and nothing else. " 
                     + "Categories \n") + prompt_cat_list + "\n" + prompt_private_info

    openai.organization = os.environ['OPENAI_ORG_ID']
    openai.api_key = os.environ['OPENAI_API_KEY']
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": content_system},
        {"role": "user", "content": "Expense description: " + desc}]
    )
    data = completion.choices[0].message

    return data["content"]