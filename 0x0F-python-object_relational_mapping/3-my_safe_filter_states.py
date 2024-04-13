#!/usr/bin/python3

'''Fixing SQL injection from the previous task
'''
import sys
import MySQLdb

def main():
    if len(sys.argv) != 5:
        sys.exit(1)

    user = sys.arg
