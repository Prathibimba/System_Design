import psycopg2
from psycopg2 import sql
import os

def create_connection():
    """
    Function to establish a connection to the PostgreSQL database.
    :return: psycopg2 connection object
    """
    try:
        connection = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),  # Database name
            user=os.getenv('DB_USER'),    # Database user
            password=os.getenv('DB_PASSWORD'),  # Database password
            host=os.getenv('DB_HOST', 'localhost'),  # Host where DB is running (default to localhost)
            port=os.getenv('DB_PORT', 5432)  # Default port for PostgreSQL
        )
        print("Connection to the database established successfully!")
        return connection

    except Exception as error:
        print(f"Error while connecting to PostgreSQL: {error}")
        return None

def create_table():
    """
    Example function to create a table in the database.
    :return: None
    """
    connection = create_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS containers (
        container_id SERIAL PRIMARY KEY,
        container_name VARCHAR(255) NOT NULL,
        destination VARCHAR(255) NOT NULL,
        arrival_time TIMESTAMP NOT NULL
    );
    '''

    try:
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully!")

    except Exception as error:
        print(f"Error while creating table: {error}")

    finally:
        cursor.close()
        connection.close()


def get_connection():
    """
    Function to get a reusable database connection.
    :return: psycopg2 connection object
    """
    return create_connection()


# Example usage
if __name__ == '__main__':
    create_table()
