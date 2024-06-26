#!/usr/bin/python3
''' This module contains a script that lists all State objects from the
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
        stateName: the state name
    '''
    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(userName, passWord, dbName),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        state = session.query(State).filter(State.name == stateName
                                                 ).order_by(State.id).first()
        if state:
            print('{}'.format(state.id))
        else:
            print('Not found')

    except Exception as e:
        print(e)
    finally:
        session.close()


if __name__ == '__main__':
    if len(argv) == 4:
        fetch_all(argv[1], argv[2], argv[3])
    else:
        print('Usage: {} username password database'.format(argv[0]))
