#!/usr/bin/python3

"""
    A script that lists all states from the database hbtn_0e_0_usa
    starting with capital letter N
    Username, password and database names are given as user args
"""


from sys import argv
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host='localhost',
                         port=3306)

    cursor = db.cursor()

    sql = """SELECT * FROM states
          WHERE name = %s
          ORDER BY id ASC"""

    cursor.execute(sql, (argv[4],))

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
