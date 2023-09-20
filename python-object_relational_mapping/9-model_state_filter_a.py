#!/usr/bin/python3
""" lists elements that contains an 'a'   """
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

    for row in result:
        if 'a' in row.name:
            print("{}: {}".format(row.id, row.name))
