import psycopg2 as pg
import Constants as c
import Table as t
import Database as db
import json

with open('conn.json') as f:
    c.Connection = json.load(f)

print(c.Connection)
d = db.Database(c.Connection['dbname'], 
                c.Connection['host'], 
                c.Connection['user'], 
                c.Connection['pword'])

d.connect()

d.ChangeQuery(c.Queries['Insert'] + " INTO budgets(budget_start_date, total_income, total_liability) VALUES(DATE '2021-10-1', '10000', '5000')")



d.close() " * FROM " + val))


for t in tables:
    for row in t:
        print(row)

print("dumping")
