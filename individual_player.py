import sqlite3   

#Connect to the database
connection = sqlite3.connect('magic_database.db')
       
       #create the cursor to access the databae
c = connection.cursor()
#Returns players details by searching last name.
def players_last_name():

#Connect to the database
       connection = sqlite3.connect('magic_database.db')
       
#create the cursor to access the databae
       c = connection.cursor()
       
#Ask database to return the player by searching last name.
       c.execute("SELECT * FROM players WHERE l_name LIKE ?", ('%' + l_name + '%',))
       return c.fetchall()
    
l_name = input ("Players Last Name or type 'exit' to go back to start: ")

if l_name != l_name:
  print("No player listed with that name in the database, please check spelling.")  
    
players = players_last_name()
for player in players:
  print(player)

    

#Commit our commands
connection.commit()
#close connection at end of instance
connection.close()

