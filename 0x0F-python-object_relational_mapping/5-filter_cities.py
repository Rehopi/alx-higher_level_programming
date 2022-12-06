#!/usr/bin/python3
"""This module contains a script that lists all cities of a passed state"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities LEFT OUTER JOIN states" +
                " ON cities.state_id=states.id" +
                " WHERE states.name='{}'".format(sys.argv[4]))
    query_rows = cur.fetchall()
    print(", ".join([row[0] for row in query_rows]))
    cur.close()
    conn.close()
