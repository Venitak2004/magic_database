import sqlite3
#Connect to the database
#connection = sqlite3.connect('magic_database.db')

#create the cursor to access the databae
#c = connection.cursor() 

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

#Insert individual player
#c.execute("INSERT INTO players VALUES ('80856857', 'Jackson', 'Josh', '02/01/2008', 'U16 FQ', '3000', '0413 662 741', 'joshua_j@iinet.com')")
#print("Player has been inserted to database. ")

#many_players = [
#                  ('12549658', 'Sinjat', 'Sean', '12/05/2008', 'U16FQ', '3000', '0412586714', 's_sinjat@cisco.com'),
#                  ('25836914', 'Cash', 'Cooper', '17/09/2008', 'U16FQ', '3000', '0452369874', 'coopercash@pbc.edu.au'),
                 
#]

#c.executemany("INSERT INTO players VALUES(?,?,?,?,?,?,?,?)", many_players)
#print("Player has been inserted to database. ")

#Query the database to check our inputs
#c.execute("SELECT * FROM players WHERE l_name LIKE 'Smith'")

#each_item = c.fetchall()

#for item in each_item:
#       print (item)

c.execute(""" UPDATE players SET ffa_id = '93651247'
          WHERE rowid = 10
          """)

c.execute("SELECT rowid, * FROM players")

each_item = c.fetchall()

for item in each_item:
       print (item)

#Returns all records from the database query
def show_all()
       #Connect to the database
       connection = sqlite3.connect('magic_database.db')
       
       #create the cursor to access the databae
       c = connection.cursor() 

       #ask queries of the database
       c.execute("SELECT rowid, * FROM players")
       each_item = c.fetchall()
       #loop through and print each line of the database
       for item in each_item:
       print (item)
       
       
       #close connection at end of instance
       connection.close()
