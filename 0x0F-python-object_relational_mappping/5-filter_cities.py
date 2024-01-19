#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb


def main():
    """
    Main function that connects to the MySQL server
    and lists cities by state.
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

        # Execute the query to retrieve cities of the given state
        query = """
            SELECT cities.name
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id
        """
        cursor.execute(query, (state_name,))

        # Fetch all rows and display results
        cities = cursor.fetchall()
        city_names = [city[0] for city in cities]
        print(", ".join(city_names))

        # Close the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
