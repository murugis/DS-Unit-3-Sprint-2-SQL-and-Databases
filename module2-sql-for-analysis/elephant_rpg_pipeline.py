import psycopg2

DB_NAME ='cxbdhsfl'
DB_USER = 'cxbdhsfl'
DB_PASS = 'b6RE3vdyeaNT4Es_Yk2t4VGIrPDXWd86'
DB_HOST = 'otto.db.elephantsql.com'

conn = psycopg2.connect(dbname = DB_NAME,
                        user = DB_USER,
                        password = DB_PASS,
                        host = DB_HOST)

cursor = conn.cursor()

cursor.execute('SELECT * FROM test_table')

results = cursor.fetchall()
#print(results)

import sqlite3

s1_conn = sqlite3.connect('rpg_db.sqlite3')
s1_cursor = s1_conn.cursor()
characters = s1_cursor.execute('SELECT * FROM  charactercreator_character;').fetchall()
print(characters)

create_character_table_query = '''
CREATE TABLE IF NOT EXISTS rpg_characters (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT, 
    intelligence INT,
    dexterity INT,
    wisdom INT
)
'''

cursor.execute(create_character_table_query)
conn.commit()

for character in characters:
    insert_query = f'''INSERT INTO rpg_characters
    (character_id,name,level,exp,hp,strength, intelligence,dexterity,wisdom) VALUES
    {character}
    '''
    cursor.execute(insert_query)

conn.commit()



