import sqlite3

conn = None
cursor = None

try:
    conn = sqlite3.connect('/no/such/folder/wombats.db')
except sqlite3.DatabaseError as err:
    print(err)
    exit()
else:
    cursor = conn.cursor()
    # query database here...
finally:
    if conn:
        conn.close()
    if cursor:
        cursor.close()
