#!/usr/bin/python3

'''A module to select all states from a database
and print out the values
'''
import sys
import MySQLdb
def main():
    '''Function to execute the procces'''
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host='localhost', port=3306, user=user,
                         passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}')")
if __name__ == '__main__':
    main()
