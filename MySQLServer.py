import mysql.connector

def create_database():
    try:
        # Establish a database connection
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Frank0268'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except mysql.connector.Error:
        print(f"Error: '{mysql.connector.Error}'")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

