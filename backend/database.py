import mysql.connector
from mysql.connector import Error
import os

class DatabaseConnection:
    def __init__(self):
        self.host = 'localhost'
        self.database = 'student_management_system'
        self.user = 'root'
        self.password = '2042124064'  # Change this to your MySQL root password
        
    def get_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                autocommit=False,
                connection_timeout=10
            )
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            print("Please make sure MySQL server is running and credentials are correct.")
            return None
    
    def execute_query(self, query, params=None):
        connection = self.get_connection()
        if connection:
            cursor = None
            try:
                cursor = connection.cursor(dictionary=True)
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                
                if query.strip().upper().startswith('SELECT'):
                    result = cursor.fetchall()
                    return result
                else:
                    connection.commit()
                    return cursor.lastrowid
            except Error as e:
                print(f"Error executing query: {e}")
                print(f"Query: {query}")
                print(f"Params: {params}")
                if connection:
                    connection.rollback()
                return None
            finally:
                if cursor:
                    cursor.close()
                if connection and connection.is_connected():
                    connection.close()
        return None
    
    def call_procedure(self, proc_name, params=None):
        connection = self.get_connection()
        if connection:
            cursor = None
            try:
                cursor = connection.cursor(dictionary=True)
                if params:
                    cursor.callproc(proc_name, params)
                else:
                    cursor.callproc(proc_name)
                
                connection.commit()
                
                # Fetch results if any
                results = []
                for result in cursor.stored_results():
                    results.extend(result.fetchall())
                
                return results if results else True
            except Error as e:
                print(f"Error calling procedure: {e}")
                print(f"Procedure: {proc_name}")
                print(f"Params: {params}")
                if connection:
                    connection.rollback()
                return None
            finally:
                if cursor:
                    cursor.close()
                if connection and connection.is_connected():
                    connection.close()
        return None
