import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="u713542740_dimaipatii",         # your username
                     passwd="*c1Ao3nY",  # your password
                     db="u713542740_Time")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM YOUR_TABLE_NAME")

# print all the first cell of all the rows
for row in cur.fetchall():
    print(row[0])

db.close()