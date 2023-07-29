#!/usr/bin/python3
""" delete a State that conmtains a  """
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import delete


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    query_all = session.query(State).all()

    for row in query_all:
        if 'a' in row.name:
            session.query(State).filter(State.id == row.id).delete()

    session.commit()
