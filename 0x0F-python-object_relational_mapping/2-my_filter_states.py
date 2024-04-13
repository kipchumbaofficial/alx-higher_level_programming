#!/usr/bin/python3
'''
A script that take an argument
Selects from database based on the argument
'''
import sys
import MySQLdb


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name\
                 LIKE BINARY {} ORDER BY id".format("'" + searched + "'"))
    rows = cur.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}')")


if __name__ == '__main__':
    main()
