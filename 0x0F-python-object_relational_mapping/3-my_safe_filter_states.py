#!/usr/bin/python3

'''Fixing SQL injection from the previous task
'''
import sys
import MySQLdb


def main():
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=user,
                         passwd=password, db=database)
    cur = db.cursor()
    searched = searched.replace("'", "''")
    query = "SELECT * FROM states WHERE name "
    query += "LIKE BINARY '%{}%' ORDER BY id".format(searched)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}')")


if __name__ == '__main__':
    main()
