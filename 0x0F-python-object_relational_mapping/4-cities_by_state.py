#!/usr/bin/python3
''' This module is used to select all the cities from the database'''
import MySQLdb
import sys


def filterStates(userName: str, password: str, dbName: str) -> None:
    ''' This function lists all the cities'''

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=userName,
                             passwd=password, db=dbName, charset="utf8")
        cur = db.cursor()
        query = "SELECT cities.id, cities.name, states.name FROM cities\
                JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC;"
        cur.execute(query)

        rows = cur.fetchall()

        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))

    finally:
        cur.close()
        db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        filterStates(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: {} username password database name".format(sys.argv[0]))
