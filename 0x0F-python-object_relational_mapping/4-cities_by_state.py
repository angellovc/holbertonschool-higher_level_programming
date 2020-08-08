#!/usr/bin/python3
"""ists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys
if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor_db = db.cursor()
    cursor_db.execute(
        "SELECT cities.id, cities.name, states.name\
        FROM cities\
        LEFT JOIN states\
        ON cities.state_id = states.id;"
    )
    states = cursor_db.fetchall()
    for state in states:
        print(state)
    cursor_db.close()
    db.close()
