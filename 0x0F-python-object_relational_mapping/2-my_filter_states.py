#!/usr/bin/python3
"""displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys
if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor_db = db.cursor()
    cursor_db.execute(
        "SELECT * FROM states WHERE name = '{}'".format(sys.argv[4]))
    states = cursor_db.fetchall()
    for state in states:
        print(state)
    cursor_db.close()
    db.close()
