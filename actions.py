from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests
import json
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


class GetIpAddrReputation(Action):

    def name(self):
        return "get_ipaddr_reputation"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        
        dispatcher.utter_message(
            "Report has been mailed. Thanks for your valuable time")
        return [SlotSet("ipAddr", userIpAddr)]


class SubscribeUser(Action):
    def name(self):
        return "subscribe_user"

    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]

        subscribe = tracker.get_slot('subscribe')
        if subscribe == "True":
            response = "You're successfully subscribed"
        if subscribe == "False":
            response = "You're successfully unsubscribed"

        dispatcher.utter_message(response)
        return [SlotSet("subscribe", subscribe)]


class GetEventDetails(Action):
    def name(self):
        return "get_event_details"

    def run(self, dispatcher, tracker, domain):
        eventId = tracker.get_slot('eventId')
        response = "Event Details of eventId" + eventId
        dispatcher.utter_message(response)
        return [SlotSet("eventId", eventId)]
