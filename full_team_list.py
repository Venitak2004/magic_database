#Full team list with row id in the table

c.execute("SELECT rowid, * FROM players")

each_item = c.fetchall()

for item in each_item:
       print (item)

#Print team list in alphabetical order
c.execute("SELECT rowid, * FROM players ORDER BY l_name")

each_item = c.fetchall()

for item in each_item:
       print (item)


#Print team list based on team name
c.execute("SELECT rowid, * FROM players WHERE team = "U16FQ")

each_item = c.fetchall()

for item in each_item:
       print (item)


