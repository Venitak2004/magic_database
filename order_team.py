import sqlite3
#Connect to the database
connection = sqlite3.connect('magic_database.db')
       
       #create the cursor to access the databae
c = connection.cursor()
#Returns team details by searching team name.

def alphabetical_team_list()
    c.execute("SELECT team FROM players ORDER BY rating DESC")
    