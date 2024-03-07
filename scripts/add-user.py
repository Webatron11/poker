from sqlite3 import connect

conn = connect('database.db')
cur = conn.cursor()

playername = input("What is the new player's name? ").lower()

cur.execute('alter table poker add %s;' % playername)
conn.commit()
