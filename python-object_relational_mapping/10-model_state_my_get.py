#!/usr/bin/python3
""" lists id of a state name given   """
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).all()

    found = 0
    for row in result:
        if row.name == argv[4]:
            found = 1
            print("{}".format(row.id))

    if found == 0:
        print("Not found")
