#!/usr/bin/python3
''' This module contains a script that  script that lists all State objects,
    and corresponding City objects, contained in the database using
    SQLAlchemy'''
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def add_state_city(userName: str, passWord: str, dbName: str) -> None:
    ''' lists all
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
        cities = session.query(City).order_by(City.id).all()
        for c in cities:
            print("{}: {} -> {}".format(c.id, c.name, c.state.name))

    except Exception as e:
        print(e)
    finally:
        pass


if __name__ == '__main__':
    add_state_city(argv[1], argv[2], argv[3])
