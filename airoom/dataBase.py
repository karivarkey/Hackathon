import sqlite3 as sql

def createDatabase(databaseName):
    con = sql.connect(databaseName)
    con.close()

def createTable(databaseName,userName):
    con = sql.connect(databaseName)
    con.execute("""CREATE TABLE IF NOT EXISTS {} (
        id INTEGER PRIMARY KEY,
        Title TEXT,
        Date TEXT,
        Time TEXT,
        Tag TEXT,
        Notes TEXT,
        Topic TEXT
    )""".format(userName))
    con.close()
createDatabase("user")
createTable("user","karivarkey")