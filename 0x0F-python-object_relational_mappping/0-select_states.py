#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb


def main():
    """
    Main function that connects to the MySQL server and lists states.
    """
    if len(sys.argv) != 4:
        print("""Usage: ./0-select_states.py
            [mysql_username]
            [mysql_password]
            [database_name]""")
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

        # Execute the query to retrieve states
        query = "SELECT * FROM states ORDER BY id"
        cursor.execute(query)

        # Fetch all rows and display results
        states = cursor.fetchall()
        for state in states:
            print(state)

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
