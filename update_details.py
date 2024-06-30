import sqlite3
connection = sqlite3.connect('magic_database.db')
       
#create the cursor to access the databae
c = connection.cursor() 


def update_player():
#Connect to the database
     connection = sqlite3.connect('magic_database.db')
       
#create the cursor to access the databae
     c = connection.cursor() 

#c.execute('''UPDATE players SET l_name = "Prosperi"
 #         WHERE rowid = 15
 #       ''')
     c.execute("UPDATE rowid, * FROM players WHERE l_name LIKE ?", ('%' + l_name + '%',))
     return c.fetchall()


l_name = input ("Which row would you like to amend?: ")


items = c.fetchall()
for item in items:
    print(item)

players = update_player()
for player in players:
  print(player)

rowid = input("Select row id to make changes: ")
ffa_id = input("Change Players FFA Number: ")
l_name = input("Change Players Last Name: ")
f_name = input("Change players first name: ")
dob = input("Change Players Date of Birth: ")
team = input("Change players allocated team: ")
fee_amount = input("Update payment fee: ")
mobile = input("Change mobile number: ")
email = input("Change email: ")


c.executemany('''
              UPDATE players SET (rowid, ffa_id, l_name, f_name, dob, team, fee_amount, mobile, email)''', players)