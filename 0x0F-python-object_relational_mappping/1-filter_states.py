#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb


def main():
    """
    Main function that connects to the MySQL server and lists filtered states.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> "
              "<database_name>".format(sys.argv[0]))
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute the query to retrieve filtered states
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(query)

        # Fetch all rows and display results
        states = cursor.fetchall()
        for state in states:
            if state[1][0] == "N":
                print(state)

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
