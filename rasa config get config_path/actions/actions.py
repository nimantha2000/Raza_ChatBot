# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import web_scraper  # Import your web scraping code

class WebScrapingAction(Action):
    def name(self):
        return "action_web_scrape"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        # Define the website URL you want to scrape
        website_url = "https://en.wikipedia.org/wiki/Ceylon_Electricity_Board"

        # Call your web scraping function from webscraper.py with the website URL
        scraped_data = web_scraper.scrape_website(website_url)

        # Send the scraped data as a response
        dispatcher.utter_message(text=scraped_data)
        return []

