import mysql.connector

class DatabaseConnector:
    def __init__(self, config):
        self.connection = mysql.connector.connect(**config)
    
    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()