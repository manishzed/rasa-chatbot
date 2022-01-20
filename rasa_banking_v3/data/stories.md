## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_name <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 

## story_name
* names{"name":"Sam"}
 - utter_greet
 
 
## story_banking
* accounts
 - utter_open_account
 - utter_ask_contact
* contacts{"contact":"9876543110"}
 - utter_ask_email
* emails{"email":"bot-fan@bots.com"}
 - utter_ask_age
* ages{"age":"26"}
 - utter_ask_pincode
* pincodes{"pincode":"302022"}
 - utter_ask_address
* addresses{"address":"shankar vihar colony"}
 - utter_ask_aadhar
* aadhars{"aadhar":"987654311000"}
 - utter_submit
 - utter_submit_rasa_db
* affirm
 - action_rasa_db
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye 
 

 
## story_test_v3
* contacts{"contact":"9876543110"}
 - utter_ask_email
* emails{"email":"bot-fan@bots.com"}
 - utter_ask_age
* ages{"age":"26"}
 - utter_ask_pincode
* pincodes{"pincode":"302022"}
 - utter_ask_address
* addresses{"address":"shankar vihar colony"}
 - utter_ask_aadhar
* aadhars{"aadhar":"987654311000"}
 - utter_submit
 - utter_submit_rasa_db
* affirm
 - action_rasa_db
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye 
 
## story_test_v4
* emails{"email":"bot-fan@bots.com"}
 - utter_ask_age
* ages{"age":"26"}
 - utter_ask_pincode
* pincodes{"pincode":"302022"}
 - utter_ask_address
* addresses{"address":"shankar vihar colony"}
 - utter_ask_aadhar
* aadhars{"aadhar":"987654311000"}
 - utter_submit
 - utter_submit_rasa_db
* affirm
 - action_rasa_db
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye 
 
## story_test_v5
* ages{"age":"26"}
 - utter_ask_pincode
* pincodes{"pincode":"302022"}
 - utter_ask_address
* addresses{"address":"shankar vihar colony"}
 - utter_ask_aadhar
* aadhars{"aadhar":"987654311000"}
 - utter_submit
 - utter_submit_rasa_db
* affirm
 - action_rasa_db
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye 
 
## story_test_v6
* pincodes{"pincode":"302022"}
 - utter_ask_address
* addresses{"address":"shankar vihar colony"}
 - utter_ask_aadhar
* aadhars{"aadhar":"987654311000"}
 - utter_submit
 - utter_submit_rasa_db
* affirm
 - action_rasa_db
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye

## story_test_v7
* addresses{"address":"shankar vihar colony"}
 - utter_ask_aadhar
* aadhars{"aadhar":"987654311000"}
 - utter_submit
 - utter_submit_rasa_db
* affirm
 - action_rasa_db
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye

## story_test_v8
* aadhars{"aadhar":"987654311000"}
 - utter_submit
 - utter_submit_rasa_db
* affirm
 - action_rasa_db
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye

## story_test_v9
* affirm
 - action_rasa_db
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye

## story_test_v10
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye

 
## story_credit_card
* credit_cards
 - utter_open_credit_card
 - utter_ask_contact
* contacts{"contact":"9876543110"}
 - utter_credit_eligibility
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye 
 
 
## story_thanks
* thanks
 - utter_thanks

## story_goodbye
* goodbye
 - utter_goodbye