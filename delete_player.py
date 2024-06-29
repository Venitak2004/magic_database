import database


#Delete a player from the database, this needs to be an option if a player changes clubs

c.execute("delte FROM players WHERE rowid = (?)")

connection.commit()

each_items = c.fetchall()

for item in each_items:
    print (item)