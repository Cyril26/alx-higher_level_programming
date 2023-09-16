#!/usr/bin/python3
"""script that lists all states with a name starting
    with N from hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM state\
                 WHERE name LIKE BINARY 'N%'\
                 ORDER BY id ASC")
    data = cur.fetchall()
    for row in data:
        print(row)

    cur.close()
    db.close()
