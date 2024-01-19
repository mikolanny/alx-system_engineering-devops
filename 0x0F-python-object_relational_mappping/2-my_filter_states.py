#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import sys
import MySQLdb


def main():
    """
    Main function that connects to the MySQL server
    and displays filtered states.
    """
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> "
              "<database_name> <state_name>".format(sys.argv[0]))
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database)
        cursor = db.cursor()

        # Execute the query to retrieve filtered states
        query = ("SELECT * FROM states WHERE name LIKE '{}' "
                 "ORDER BY id".format(state_name))
        cursor.execute(query)

        # Fetch all rows and display results
        states = cursor.fetchall()
        for state in states:
            if state[1] == state_name:
                print(state)

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
