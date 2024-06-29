#Update player details in the database 

c.execute(""" UPDATE players SET f_name = 'Cruze'
          WHERE l_name = 'Smith'
          """)
