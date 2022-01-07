#Rasa slot filling example either from entities and action slot. 

#run flask api response on html

#to run both rasa server i.e rasa nlu and rasa core

#error free

* first create and train model

----- rasa init

----- rasa train

1> if want to chat with actions functionalities  using endpoint on postman or flask APIs or for deployment purpose use this

#step1: Terminal 1

rasa run --enable-api --log-file out.log --cors "*"

rasa run --enable-api --log-file out.log --cors "*" --debug

step2: Terminal 2

rasa run actions

or 

python -m rasa_sdk.endpoint --actions actions

finally:

then run url on postman

http://localhost:5005/webhooks/rest/webhook/

#json content":

{"message": "how are you?"}


2> if want to chat on terminal with actions functionalities


step1: terminal 1

python -m rasa_sdk.endpoint --actions actions


step2 : terminal 2

rasa shell


3> if only want to run only rasa or for simple chat on terminal without using or running action functionalities

simple run on terminal: 

1> rasa init  ----------for rasa file creations if already created ignore this

2> rasa train  --------- to train rasa model

3> rasa shell   -----  to chat on terminal

