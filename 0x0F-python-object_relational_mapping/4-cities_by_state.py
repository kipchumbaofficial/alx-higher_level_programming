#!/usr/bin/python3
'''Script that lists all cities
from a database
'''
import MySQLdb
from sys import argv


def main():
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database)
    cur = db.cursor()
    query = "SELECT cities.*, states.name AS states_name "
    query += "FROM cities "
    query += "JOIN states ON cities.state_id=states.id"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[2]}', '{row[3]}')")


if __name__ == '__main__':
    main()
