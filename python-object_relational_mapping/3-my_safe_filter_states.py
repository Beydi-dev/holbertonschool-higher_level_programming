#!/usr/bin/python3
"""
Lists all states where name matches the argument (safe from SQL injection)
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC",
        (sys.argv[4],)
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
