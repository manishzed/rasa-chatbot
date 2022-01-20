#Rasa slot filling example either from entities and action slot. 

#installation with setup dependecies:

step 1> Build python Environment:

  a> pip install virtualenv: to install virtualenv

  b> virtualenv env_name: create vitual environment

  c> env_name\Scripts\activate: to activate env

step 2:> Now install RASA packages and its dependencies:

  a> pip install rasa==1.10.25

  b> pip install tensorflow==2.1.4

  c> pip install spacy==2.3.5

#run flask api response on html

#to run both rasa server i.e rasa nlu and rasa core

# have created sqlite database to store some data like name, email, age, pincode...etc. buils class function on actions.py to store and shows data

#error free

first create and train model

----- rasa init

----- rasa train

#to run both rasa server i.e rasa nlu and rasa core

#error free

#step1:

rasa run --enable-api --log-file out.log --cors "*"

rasa run --enable-api --log-file out.log --cors "*" --debug

step2:

rasa run actions --debug

finally:

then run url on postman

http://localhost:5005/webhooks/rest/webhook/

#json content":

{"message": "hi"}
