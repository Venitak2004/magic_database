import sqlite3

#Connect to the database
connection = sqlite3.connect('magic_database.db')
       
       #create the cursor to access the databae
c = connection.cursor()
#Returns team details by searching team name.
def full_team():
       #Connect to the database
       connection = sqlite3.connect('magic_database.db')
       
       #create the cursor to access the databae
       c = connection.cursor()
       
       #Ask database to return the team by searching for team name.
       c.execute("SELECT * FROM players WHERE team LIKE ?", ('%' + team + '%',))
       return c.fetchall()
    
team = input ("Team Name or type 'exit' to quit: ")
    
teams = full_team()
for team in teams:
  print(team)
#if player not in players:
#  print("No player with that last name in the database, please check spelling.")      

#Commit our commands
connection.commit()
#close connection at end of instance
connection.close()

