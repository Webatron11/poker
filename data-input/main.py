from dateutil import *
import psycopg2 as psql
import json

with open('connection.json') as f:
    connectioninfo = json.load(f)

conn = psql.connect(database="poker", user=connectioninfo['user'], password=connectioninfo['password'], host=connectioninfo['host'], port=connectioninfo['port'])
cur = conn.cursor()

cur.close()
conn.close()
