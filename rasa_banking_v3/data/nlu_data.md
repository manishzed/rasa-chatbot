## intent:goodbye <!--- The label of the intent --> 
- Bye 			<!--- Training examples for intent 'bye'--> 
- Bye bot
- bye
- bye for now
- Bye bot
- bye
- bye for now
- Bye bot
- bye
- bye for now
- Bye bot
- bye
- bye for now
## intent:greet
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- hi again
- hi there
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- hi again
- hi there
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- hi again
- hi there
- hi
- hey
- hi bot
- hey bot
- hello
- Hi again
- Hi there
- hi
- hey
- hi bot
- hey bot
- hello
- Hi again
- Hi there
- hi
- hey
- hi bot
- hey bot
- hello
- Hi again
- Hi there

## intent:thanks
- Thanks
- Thank you
- Thank you so much
- Thanks 
- Thanks for that
- Thanks
- Thank you
- Thank you so much
- Thanks 
- Thanks for that
- thanks
- thank you
- thank you so much
- thanks 
- thanks for that
- thanks
- thank you
- thank you so much
- thanks 
- thanks for that
- thanks
- thank you
- thank you so much
- thanks 
- thanks for that

## intent:affirm
- yes
- yes sure
- absolutely
- for sure
- yes yes yes
- definitely
- yes
- yes sure
- absolutely
- for sure
- yes yes yes
- definitely


## intent:names
- My name is [Tatiana](name)  <!--- Square brackets contain the value of entity while the text in parentheses is a a label of the entity --> 
- I am [Josh](name)
- My name is [John](name)
- Name name is [Tom](name)
- I am [Richard](name)
- I am [Philipp](name)
- I am [Charlie](name)
- i am [manish](name)
- my name is [manish](name)
- [manish](name)
- [jay](name)
- My name is [Tatiana](name)  <!--- Square brackets contain the value of entity while the text in parentheses is a a label of the entity --> 
- I am [Josh](name)
- My name is [John](name)
- Name name is [Tom](name)
- I am [Richard](name)
- I am [Philipp](name)
- I am [Charlie](name)
- i am [manish](name)
- my name is [manish](name)
- [manish](name)
- [ishmk](name)

## intent:accounts
- deposit account
- open a personal deposit account
- account
- open an account
- deposit account
- client wants to open an acccount
- help me to find an account
- a version of account
- types of accounts
- show ne types of accoutnt
- show me some types of accounts
- please, tell me about types of accounts
- print info about accounts
- deposit account
- open a personal deposit account
- account
- open an account
- deposit account
- client wants to open an acccount
- help me to find an account
- a version of account
- types of accounts
- show ne types of accoutnt
- show me some types of accounts
- please, tell me about types of accounts
- print info about accounts




## intent:contacts
- my number is [9876543110](contact)
- my mobile is [8346586739](contact)
- my number is [6367251643](contact)
- my mobile is [6356231542](contact)
- my number is [7208765441](contact)
- my mobile is [9999999999](contact)
- [7856483765](contact)
- [2222222222](contact)
- [6666666666](contact)
- [0141270111](contact)
- [9886559009](contact)
- [9876545634](contact)
- [1023456789](contact)
- [0987654321](contact)
- [6367251632](contact)
- [7265430991](contact)
- cell no [7865456357](contact)
- call me at [7765432867](contact)
- you can call me at [9886754345](contact)
- contact me at [8309856734](contact)
- call me at [8467387675](contact)
-[8976545673] is my number
- you can call me at [9345871200](contact)
- my no. is [8876438756](contact)
- ping me on [7734563487](contact)
- whatsapp no. [7765498345](contact)


## regex:contact
- [0-9]{10}

## intent:emails
- [maxmeier@firma.de](email)
- [bot-fan@bots.com](email)
- [maxmeier@firma.de](email)
- [bot-fan@bots.com](email)
- [email@rasa.com](email)
- [fan@bots.com](email)
- [email@rasa.com](email)
- [bot@bots.com](email)
- [email@rasa.com](email)
- [info@rasa.com](email)
- [hi@rasa.com](email)
- my email is [email@rasa.com](email)
- my email is [markjobs@ibm.com](email)
- my email is [khardik.kmosu@bol.net.in](email)
- my business mail is [mikemiller@sales.apple.com](email)
- email = [stephanywhite@microsoft.com](email)
- mail: [julianfrank@hotmail.com](email)
- [santaklaus@googlemail.com](email)
- [saswatkarhar@rediffmail.com](email)
- [nerd@stanford.edu](email)
- [alexander.denker@tu-berlin.de](email)
- [sislawawa@india.com](email)

## intent:ages
- my age is [24](age)
- my age is [25](age)
- my age is [26](age)
- my age is [27](age)
- my age is [28](age)
- my age is [30](age)
- [23](age) years old
- [24](age) 
- [45](age) 
- [26](age) 
- [27](age) 
- [28](age) 
- [29](age) 
- [30](age) 
- [24](age) 
- [45](age) 
- [1](age) 
- [2](age) 
- [99](age) 
- [32](age) 
- [31](age) 
- [32](age) years
- [33](age) years
- [50](age) years
- [41](age) years
- [57](age) years
- [56](age) years
- my age is [56](age)
- my age is [52](age)
- my age is [62](age)
- my age is [72](age)
- my age is [83](age)
- my age is [67](age)
- [68](age) years old
- [69](age) 
- [77](age) 
- [87](age) 
- [98](age) 
- [91](age) 
- [90](age) 
- [80](age) 

## regex:age
- [0-9]{2}

## intent:pincodes
- [302029](pincode)
- [111111](pincode)
- [123980](pincode)
- [123090](pincode)
- [098765](pincode)
- [112233](pincode)
- [825317](pincode)
- [000000](pincode)
- [123980](pincode)
- [555555](pincode)
- [825322](pincode)
- [333333](pincode)
- my pincode is [123456](pincode)
- my pincode is [302022](pincode)
- my pincode is [302021](pincode)
- my pincode is [825301](pincode)
- my pincode is [302028](pincode)
- my pincode is [302026](pincode)

## regex:pincode
- [0-9]{6}


## intent:addresses
- [shankar colony](address)
- [shankar nagar](address)
- [shankar vihar colony](address)
- [shankar vihar colony](address)
- [123/567 gopalpura pani](address)
- i live at [triveni chourah](address)
- my address is [45/567, near goovernment hospital](address)
- i live at [PTC road](address)
- my address is [near goovernment hospital](address)
- [malviya nagar](address)
- [matwari road](address)
- [jagatpura road](address)
- [sitapura tonk road](address)
- [mansarovar](address)
- [Matwari road](address)
- [malviya nagar](address)
- [bhavnagar gujarat](address)
- [bhav nagar gujarat](address)
- [the mall road himachal paradesh](address)
- [sarojni nagar delhi](address)
- [bhavnagar](address)
- [bhav nagar](address)

## intent:aadhars
- my aadhar number is [987654311000](aadhar)
- my aadhar is [834658673911](aadhar)
- my aadhar number is [987654311000](aadhar)
- my aadhar is [834658673911](aadhar)
- my aadhar number is [323101353000](aadhar)
- my aadhar is [834658673911](aadhar)
- [123456789012](aadhar)
- [098765432109](aadhar)
- [785648376522](aadhar)
- [987654563433](aadhar)
- [123456789012](aadhar)
- [098765432109](aadhar)
-[897654567355] is my aadhar number
- my aadhar no. is [887643875677](aadhar)
- my aadhar number is [112233445566](aadhar)
- my aadhar is [887766554433](aadhar)
- my aadhar number is [636725165412](aadhar)
- my aadhar is [323101353321](aadhar)
- my aadhar number is [323101353111](aadhar)
- my aadhar is [834658673911](aadhar)
- [785648376522](aadhar)
- [323101353000](aadhar)
- [222222222222](aadhar)
- [239301187612](aadhar)
- [123456789012](aadhar)
- [323109873076](aadhar)
-[897654567355] is my aadhar number
- my aadhar no. is [887643875677](aadhar)

## regex:aadhar
- [0-9]{12}

## intent:credit_cards
- want to apply for credit card
- apply for credit card
- can i apply a for credit card?
- please apply for a credit card
- pls apply for credit card
- i want to apply for credit card
- want to apply for credit card
- apply for credit card
- can i apply a for credit card?
- please apply for a credit card
- pls apply for credit card
- i want to apply for credit card


## intent:out_of_scope
- Is Rasa really smart?
- bots are bad
- I dont like bots
- Is Rasa bot smart?