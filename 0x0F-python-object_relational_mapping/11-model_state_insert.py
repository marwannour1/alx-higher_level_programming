#!/usr/bin/python3
''' This module contains a script that adds the state object louisiana to the
    database using SQLAlchemy'''

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def fetch_all(userName: str, passWord: str, dbName: str,
              stateName: str) -> None:
    ''' Fetch all states from the database
        userName: the username
        passWord: the password
        dbName: the database name
    '''
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(userName, passWord, dbName),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        newState = State(name="Louisiana")
        session.add(newState)
        session.commit()
        print(newState.id)

    except Exception as e:
        print(e)
    finally:
        session.close()


if __name__ == '__main__':
    if len(argv) == 4:
        fetch_all(argv[1], argv[2], argv[3])
    else:
        print('Usage: {} username password database'.format(argv[0]))
