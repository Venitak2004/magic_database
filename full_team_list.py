import database

#Connect to the database
connection = sqlite3.connect('magic_database.db')
#create the cursor to access the databae
c = connection.cursor() 


#Full team list with row id in the table

#c.execute("SELECT rowid, * FROM players")

#each_item = c.fetchall()

#for item in each_item:
       print (item)

#Print team list in alphabetical order
#c.execute("SELECT rowid, * FROM players ORDER BY l_name")

#each_item = c.fetchall()

#for item in each_item:
 #      print (item)


def team_list(team):
       
      #Connect to the database
      connection = sqlite3.connect('magic_database.db')
      #create the cursor to access the databae
      c = connection.cursor() 
      #Print team list based on team name

      c.execute("SELECT * FROM players WHERE team = input('team: ')")

      each_item = c.fetchall()

      for item in each_item:
         print (item)


