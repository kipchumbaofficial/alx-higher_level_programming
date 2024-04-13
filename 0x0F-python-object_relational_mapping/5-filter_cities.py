#!/usr/bin/python3
'''
Takes in name of state
Spits all the cities in that state
'''
import MySQLdb
from sys import argv


def main():
    user = argv[1]
    password = argv[2]
    database = argv[3]
    state = argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=user,
                         passwd=password, db=database)
    cur = db.cursor()
    state = state.replace("'", "''")
    query = "SELECT cities.* FROM cities "
    query += "LEFT JOIN states ON cities.state_id=states.id "
    query += "WHERE states.name LIKE BINARY '%{}%'".format(state)
    query += "ORDER BY cities.id"
    cur.execute(query)
    rows = cur.fetchall()

    for i, row in enumerate(rows):
        print(row[2], end="")
        if i < len(row) - 1:
            print(', ', end="")
    print()


if __name__ == '__main__':
    main()
