#!/usr/bin/python3
"""This module contains a script that lists all states starting with N"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cmd = """SELECT * FROM states WHERE Name LIKE BINARY '{}' ORDER BY id ASC"""
    cur.execute(cmd)
    nStates = cur.fetchall()

    for state in nStates:
        if (state[1][0] == 'N'):
            print(state)

    cur.close()
    db.close()
