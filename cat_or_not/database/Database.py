import sqlite3

class Database():
    def __init__(self):
        self.db_name = 'database/cat_or_not.db'
        self.schema = 'database/schema.sql'
        connection = self.get_connection()
        with open(self.schema) as file:
            connection.executescript(file.read())
        connection.commit()
        connection.close()

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def add_result(self, filename):
        connection = self.get_connection()
        connection.execute("INSERT INTO results (file_name) VALUES (?)", (filename,))
        connection.commit()
        connection.close()

    def get_result(self, id):
        connection = self.get_connection()
        result = connection.execute('SELECT file_name FROM results WHERE id = ?', (id,)).fetchone()[0]
        connection.close()
        return result

    def get_max_id(self):
        connection = self.get_connection()
        next_id = connection.execute('SELECT MAX(id) as id FROM results').fetchone()[0]
        connection.close()
        return next_id
