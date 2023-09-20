#!/usr/bin/python3
""" get citie of a state """
from model_city import City
from model_state import State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State.name, City.id, City.name).join(
        City, City.state_id == State.id).all()

    for row in query:
        print("{}: ({}) {}".format(row[0], row[1], row[2]))
    session.close()
