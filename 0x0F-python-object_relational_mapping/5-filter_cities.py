#!/usr/bin/python3
"""lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys
if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor_db = db.cursor()
    num_cities = cursor_db.execute(
        "SELECT name FROM cities\
        WHERE state_id = (SELECT id FROM states WHERE name = %s)\
        ORDER BY cities.id ASC;", (sys.argv[4], )
    )
    cities = cursor_db.fetchall()
    for city in range(0, num_cities):
        if city is not 0:
            print(", ", end="")
        print(cities[city][0], end="")
    print('')
    cursor_db.close()
    db.close()
