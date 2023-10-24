from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, Restarted, CollectingDispatcher
import requests
import bs4 as bs
import urllib.request
from typing import Dict, Text, Any, List

class ActionOpenOutageMap(Action):
    def name(self):
        return "action_open_outage_map"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open the website in the user's browser
        message = "You can check the CEB Outage Map [here](https://cebcare.ceb.lk/Incognito/OutageMap)."
        dispatcher.utter_message(text=message)

        return [Restarted()]

class ActionFetchInfo(Action):
    def name(self):
        return "action_fetch_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Send request to the website
        response = requests.get('http://www.ceb.lk')

        # Parse the response using BeautifulSoup
        soup = bs.BeautifulSoup(response.text, 'html.parser')

        # Extract the required information from the soup object
        info = soup.find('div', {'class': 'info'}).text

        # Set the extracted information as a slot
        return [SlotSet('info', info)]
