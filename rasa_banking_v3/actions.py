# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
#from rasa_core_sdk import Action
from rasa_sdk import Action

#database saving
from rasa_db import rasa_create_insert_db
logger = logging.getLogger(__name__)


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = requests.get('http://api.icndb.com/jokes/random').json() #make an apie call
        joke = request['value']['joke'] #extract a joke from returned json response
        dispatcher.utter_message(joke) #send the message back to the user
        return []


class ActionRasaDb(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_rasa_db"

    def run(self, dispatcher, tracker, domain):
        name = tracker.get_slot('name')
        contact = tracker.get_slot('contact')
        email = tracker.get_slot('email')
        age = tracker.get_slot('age')
        pincode = tracker.get_slot('pincode')
        address = tracker.get_slot('address')
        aadhar = tracker.get_slot('aadhar')
        response = "Your name:{}, contact:{}, email:{}, age:{}, pincode:{}, address:{}, aadhar:{}. what do you want else related to database?".format(name, contact, email, age, pincode, address, aadhar)
        dispatcher.utter_message(response) #send the message back to the user
        rasa_create_insert_db(name, contact, email, age, pincode, address, aadhar)
        return []
        
        
        
        