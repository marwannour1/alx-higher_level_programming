#!/usr/bin/python3
''' This module contains a script that adds the State California and City
    San Francisco to the database using SQLAlchemy'''
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def add_state_city(userName: str, passWord: str, dbName: str) -> None:
    ''' Add the state California and the city San Francisco to the database
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
        new_state = State(name='California')
        session.add(new_state)
        session.commit()
        new_city = City(name='San Francisco', state_id=new_state.id)
        session.add(new_city)
        session.commit()
    except Exception as e:
        print(e)
    finally:
        session.close()


if __name__ == '__main__':
    add_state_city(argv[1], argv[2], argv[3])
