#!/usr/bin/python3
''' This module contains a script that changes the state with id 2 to new
    mexico in database using SQLAlchemy'''

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def change(userName: str, passWord: str, dbName: str) -> None:
    ''' change state with id 2 to new mexico
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

        state = session.query(State).filter(State.id == 2).first()
        state.name = 'New Mexico'
        session.commit()

    except Exception as e:
        print(e)
    finally:
        session.close()


if __name__ == '__main__':
    if len(argv) == 4:
        change(argv[1], argv[2], argv[3])
    else:
        print('Usage: {} username password database'.format(argv[0]))
