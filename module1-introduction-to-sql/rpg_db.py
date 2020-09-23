import os
import sqlite3

#constructing a path to where to where the rpg_db database exists
DB_FILEPATH = "module1-introduction-to-sql/rpg_db.sqlite3" # this only works conditionally and you may have to run from root directory.
#
DB_FILEPATH = os.path.join(os.path.dirname(__file__),"rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)
  
breakpoint()
query = "SELECT * FROM customers;"