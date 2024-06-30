import sqlite3

#Connect to the database
connection = sqlite3.connect('magic_database.db')
#create the cursor to access the databae
c = connection.cursor() 

#Query the database for the row id to access a player.

c.execute("SELECT rowid, * FROM players")

items = c.fetchall()
for item in items:
    print(item)

      #Commit our commands
connection.commit()
       #close connection at end of instance
connection.close()
