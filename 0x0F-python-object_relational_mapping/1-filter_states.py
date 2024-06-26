#!/usr/bin/python3
'''A Script to filter and print out states
Starting with letter N from a database
'''
import MySQLdb
import sys


def main():
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}')")


if __name__ == '__main__':
    main()
