from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, Restarted, UserUttered, FollowupAction
from rasa_sdk.forms import FormAction
import re

class ActionIcpFever(Action):

    def name(self):
        return "action_icp_fever"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('')
        dispatcher.utter_message('')
        dispatcher.utter_message('')
        
class ActionIcpTightCough(Action):

    def name(self):
        return "action_icp_tight_cough"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('')
        dispatcher.utter_message('')
        dispatcher.utter_message('')
        
class ActionIcpDryCough(Action):

    def name(self):
        return "action_icp_dry_cough"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('')
        dispatcher.utter_message('')
        
        
class ActionIcpSharpPain(Action):

    def name(self):
        return "action_icp_sharp_pain"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('')
        dispatcher.utter_message('')
        
class ActionIcpHighFever(Action):

    def name(self):
        return "action_icp_high_fever"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('')
        dispatcher.utter_message('')
        
class ActionIcpPainTenderness(Action):

    def name(self):
        return "action_icp_pain_tenderness"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('')
        dispatcher.utter_message('')
        

class ContactForm(FormAction):

    def name(self):
        return "contact_form"

    @staticmethod
    def required_slots(tracker):

        return ["name","phone_number","email"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "name": self.from_text(),
            "phone_number": self.from_text(),
            "email": self.from_text(),
        }

    def validate_name(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        
        
        words = list(value.split())
        
        
        if len(words) > 2:
            dispatcher.utter_message("The name was too long.....")
            return {"name": None}
            
        for word in words:
            if word in ["don't", 'not', "no", "won't", "why"] or 'do not' in value or 'will not' in value:
                dispatcher.utter_message("We need your name to proceed further")
                return {"name": None}
        
        return {"name":value.title()}
    
    def validate_phone_number(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if (len(value) == 10 or len(value) == 12):
            try:
                number = int(value)
                return {"phone_number":number}
            except:
                dispatcher.utter_message('I am unable to find a valid mobile number')
                return {"phone_number":None}
        else:
            dispatcher.utter_message('I am unable to find a valid mobile number')
            return {"phone_number":None}
        

    
    def validate_email(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        
        res = re.findall(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', value.lower())

        if len(res)>0:
            print(res)
            return {"email":res[0]}
        else:
            dispatcher.utter_message('I am unable to find a valid email id')
            return {"email":None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        name = tracker.get_slot('name')
        phone = tracker.get_slot('phone_number')
        email = tracker.get_slot('email')
        print(name,phone,email)
        dispatcher.utter_message(text=f"Thank you for submitting the Details. Here are your details. Name: {name}, Phone: {phone} and Email: {email}. What can I do for you?")
        return []
