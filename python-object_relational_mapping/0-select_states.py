#!/usr/bin/python3
import MySQLdb
from sys import argv


if __name__ == '__main__':

    db=MySQLdb.connect("localhost", 
                  argv[1], argv[2], argv[3])


    info=db.cursor()
    info.execute("SELECT * FROM states ORDER BY states.id ASC ")

    for states in info.fetchall():
        print(states)

    db.close()


