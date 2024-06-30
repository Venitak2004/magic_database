import sqlite3

#Connect to the database
connection = sqlite3.connect('magic_database.db')
#create the cursor to access the databae
c = connection.cursor() 

#Set up table headers for the database, as this is already done I have quoted it out so you can see the code.

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

#Insert individual player - This is some of the code used to populate the database.
#c.execute("INSERT INTO players VALUES ('80856857', 'Jackson', 'Josh', '02/01/2008', 'U16 FQ', '3000', '0413 662 741', 'joshua_j@iinet.com')")
#print("Player has been inserted to database. ")

#I used this code to further populate the database with more players.
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

#c.execute(""" UPDATE players SET ffa_id = '93651247'
#          WHERE rowid = 10
#          """)

#c.execute("SELECT rowid, * FROM players")

#each_item = c.fetchall()

#for item in each_item:
#       print (item)

#Returns all records from the database query
def show_all():
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
       
       #Commit our commands
       connection.commit()
       #close connection at end of instance
       connection.close()

# Add a new player to a the database/team.       
def add_player(ffa_id, l_name, f_name, dob, team, fee_amount, mobile, email):
     #Connect to the database
     connection = sqlite3.connect('magic_database.db')
     
     #create the cursor to access the databa
     c = connection.cursor() 

     c.execute("INSERT INTO players VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (ffa_id, l_name, f_name, dob, team, fee_amount, mobile, email))
     #Commit our commands
     connection.commit()
     #Close the connection
     connection.close()
     

     

#Make changes to existing player in the database

def player_changes():
       #Connect to the database
       connection = sqlite3.connect('magic_database.db')
       
       #create the cursor to access the databae
       c = connection.cursor() 

       c.execute(""" UPDATE players SET team = 'U16JPL'
              WHERE rowid = 10
              """)

       c.execute("SELECT rowid, * FROM players")

       each_item = c.fetchall()

       for item in each_item:
           print (item)
       #Commit our commands
       connection.commit()
       #Close the connection
       connection.close()

#Delete a player from the database ***still needs work***
def player_delete():
      #Connect to the database
       connection = sqlite3.connect('magic_database.db')
       
       #create the cursor to access the databae
       c = connection.cursor() 

user_selection = input("What players row id do you want to delete: " rowid)

c.execute(" DELETE from players WHERE rowid = (user_selection)")
       
       
       #Commit our commands
connection.commit()
       #Close the connection
connection.close()       

#Asking the user to insert a new player into the database
def player_insert(ffa_id, l_name, f_name, dob, team, fee_amount, mobile, email):
       
       #Connect to the database
       connection = sqlite3.connect('magic_database.db')
       
       #Create the cursor to access the databae
       c = connection.cursor() 
       

#Ask user to input details of player
       ffa_id = input('Enter Unique FFA id number(must be 8 digits): ')
       l_name = input('Enter players last name: ')
       f_name = input('Enter players first name: ')
       dob = input('Enter players date of birth DD/MM/YYYY: ')
       team = input('Enter team player is allocated to eg U16JPL or U16FQ: ')
       fee_amount = input('Input fees paid: ')
       mobile = input('Enter contact mobile number (format 0400 123 456): ')
       email = input('Enter email address for player: ')

       c.execute('''INSERT INTO players (ffa_id, l_name, f_name, dob, team, fee_amount, mobile, email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (ffa_id, l_name, f_name, dob, team, fee_amount, mobile, email))
       #Insert player info into the database
       player_insert(ffa_id, l_name, f_name, dob, team, fee_amount, mobile, email)
       print('New Player data has been inserted successfully!')

       #Commit our commands
       connection.commit()
       #Close the connection
       connection.close()  

#Returns players details by searching last name.
def players_last_name():
       #Connect to the database
       connection = sqlite3.connect('magic_database.db')
       
       #create the cursor to access the databae
       c = connection.cursor()
       
       #Ask database to return the player by searching last name.
       c.execute("SELECT * FROM players WHERE l_name LIKE ?", ('%' + l_name + '%',))
       return c.fetchall()
       
l_name = input ("Players Last Name: ")


players = players_last_name()
for player in players:
    print(player)           

#Commit our commands
connection.commit()
#close connection at end of instance
connection.close()
