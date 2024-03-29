#!/usr/bin/python3
""" filtering states """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ filtering states """

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    info = db.cursor()

    info.execute("SELECT * FROM states ORDER BY states.id ASC ")

    for states in info.fetchall():

        if states[1][0] == 'N':
            print(states)

    db.close()
