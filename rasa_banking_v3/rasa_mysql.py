import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='rasa_db',
                                         user='root',
                                         password='')
    
    cursor = connection.cursor()
    # Creating table
    rasa_table ="""CREATE TABLE rasa_actions_db(name VARCHAR, contact VARCHAR,email VARCHAR, age VARCHAR, pincode VARCHAR, address VARCHAR, aadhar VARCHAR)"""

    cursor.execute(rasa_table)
    print("rasa_table created successfully")

    mySql_insert_query = """INSERT INTO rasa_actions_db (name, contact, email, age, pincode, address, aadhar) 
                           VALUES ("manish", 1234567890,"email@rasa.com", 25, 302022, "shankar vihar colony", 123456789012')"""

    
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into rasa_actions_db table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into rasa_actions_db table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")