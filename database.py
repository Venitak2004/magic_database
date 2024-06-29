import sqlite3
#Connect to the database
connection = sqlite3.connect('magic_database.db')

#create the cursor to access the databae
c = connection.cursor() 

#Set up table headers for the database
#c.execute("""CREATE TABLE players (
#         ffa_id text,
#         l_name text,
#         f_name text,
#         dob text,
#         team text,
#         fee_amount integer,
#         mobile text,
#         email text
#   )""")

c.execute("INSERT INTO players VALUES ('80856857', 'Jackson', 'Josh', '02/01/2008', 'U16 FQ', '3000', '0413 662 741', 'joshua_j@iinet.com')")
print("Player has been inserted to database. ")


#commit our commands
connection.commit()

#close connection at end of instance
connection.close()