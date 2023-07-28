#!/usr/bin/python3
""" filtering states by user input  """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """ filtering states by user input """

    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

    info = db.cursor()

    info.execute(
        "SELECT cities.name FROM cities \
            INNER JOIN states ON states.id = cities.state_id\
             WHERE states.name = %s ORDER BY cities.id ASC", (argv[4],))
    output = ""
    for cities in info.fetchall():
        output += cities[0] + ', '

    print(output[:-2])

    db.close()
