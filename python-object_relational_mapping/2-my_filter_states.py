#!/usr/bin/python3
""" filtering states by user input  """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ filtering states by user input """

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    info = db.cursor()

    info.execute("SELECT * FROM states ORDER BY states.id ASC ")

    for states in info.fetchall():
        if states[1] == argv[4]:
            print(states)

    db.close()
