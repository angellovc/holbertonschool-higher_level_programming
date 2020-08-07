#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys
if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor_db = db.cursor()
    cursor_db.execute("SELECT * FROM states")
    states = cursor_db.fetchall()
    for state in states:
        print(state)
    cursor_db.close()
    db.close()