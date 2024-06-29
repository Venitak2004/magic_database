import database
#This feature will add a new player to the database
#database.add_player input(("FFA No" {ffa_id}, "Last Name" {l_name}, "First Name" {f_name}, "Date of Birth" {dob}, "Team" {team}, "Fee" {fee}, "Mobile" {mobile}, "Email" {email}))

#This feature will add a new player to the database, you must pass all the variables into the table.
#database.add_player()
#This feature will print the entire database list
database.show_all()

#This feature will allow you to search for the players unique ffa no 
database.last_name()

#This feature will allow you to change the team allocation from ie U16FQ to U16JPL
database.player_changes()