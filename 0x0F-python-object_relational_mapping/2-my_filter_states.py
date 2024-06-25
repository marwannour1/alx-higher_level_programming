#!/usr/bin/python3
''' This module is used to select all the states from the database with
    a name matching the input string'''
import MySQLdb
import sys


def filterStates(userName: str, password: str, dbName: str, name: str) -> None:
    ''' This function lists all the states from the database with a name
        starting with N (upper N)'''

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=userName,
                             passwd=password, db=dbName, charset="utf8")
        cur = db.cursor()
        cur.execute(f"SELECT * FROM states WHERE name = {name} COLLATE\
                    utf8_bin ORDER BY id ASC;")

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
        print("Usage: {} username password database".format(sys.argv[0]))
