import database

#Query the database to check the database for individual players by last name.

c.execute("SELECT * FROM players WHERE l_name LIKE 'Smith'")

each_item = c.fetchall()

for item in each_item:
       print (item)

       