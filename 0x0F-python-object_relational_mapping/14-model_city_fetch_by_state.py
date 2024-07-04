#!/usr/bin/python3
''' This module contains a script that lists all City objects from the
    database using SQLAlchemy'''
from model_city import City, Base
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

def fetch_all(userName: str, passWord: str, dbName: str) -> None:
    ''' Fetch all cities from the database
        userName: the username
        passWord: the password
        dbName: the database name
    '''
    try:

        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(userName, passWord, dbName),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        for city, state in session.query(City, State).filter\
            (City.state_id == State.id).all():
            print('{}: ({}) {}'.format(state.name, city.id, city.name))
    except Exception as e:
        print(e)
    finally:
        session.close()

if __name__ == '__main__':
    fetch_all(argv[1], argv[2], argv[3])
