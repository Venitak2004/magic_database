import sqlite3
connection = sqlite3.connect('magic_database.db')
       
#create the cursor to access the databae
c = connection.cursor() 

#Delete a player from the database ***still needs work***
#def player_delete():
#Connect to the database
connection = sqlite3.connect('magic_database.db')
       
#create the cursor to access the databae
c = connection.cursor() 
c.execute('''UPDATE players SET fee_amount = '250'
          WHERE rowid = 15



''')




c.execute("SELECT rowid, * FROM players WHERE l_name = 'Prosperi'")

items = c.fetchall()
for item in items:
    print(item)

       #Commit our commands
connection.commit()
       #Close the connection
connection.close()   



