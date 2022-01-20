import sqlite3

def rasa_create_insert_db(name, contact, email, age, pincode, address, aadhar):
    connection = sqlite3.connect('rasa_.db')
    cursor = connection.cursor()
    
    # Creating table
    #rasa_table ="""CREATE TABLE rasa_actions_db_v1(name TEXT, contact TEXT,
    #email TEXT, age TEXT, pincode TEXT, address TEXT, aadhar TEXT)"""

    #cursor.execute(rasa_table)
    print("rasa_table created successfully")
    cursor.execute("""INSERT INTO rasa_actions_db_v1
                          (name, contact, email, age, pincode, address, aadhar) VALUES (?, ?, ?, ?, ?, ?, ?);""", (name, contact, email, age, pincode, address, aadhar))

    # Display data inserted
    print("Data Inserted in the table: ")
    data=cursor.execute('''SELECT * FROM rasa_actions_db''')
    for row in data:
        print(row)
  
    connection.commit()
    connection.close()
    
    
    
#if __name__ == '__main__':
#    rasa_create_insert_db("manish", 1234567890,"email@rasa.com", 25, 302022, "shankar vihar colony", 123456789012)
    
