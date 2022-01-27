import sqlite3

class Database():
    def __init__(self):
        self.db_name = 'Database/cat_or_not.db'
        self.schema = 'Database/schema.sql'
        connection = self.get_connection()
        with open(self.schema) as file:
            connection.executescript(file.read())
        connection.commit()
        connection.close()

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def add_result(self, filename, file_size, analysis_status):
        connection = self.get_connection()
        connection.execute("INSERT INTO analysis_history (file_name, file_size, analysis_status) VALUES (?, ?, ?)", (filename, file_size, analysis_status,))
        connection.commit()
        connection.close()

    def get_result(self, id):
        connection = self.get_connection()
        result = connection.execute('SELECT file_name FROM analysis_history WHERE history_id = ?', (id,)).fetchone()[0]
        connection.close()
        return result

    def get_max_id(self):
        connection = self.get_connection()
        next_id = connection.execute('SELECT MAX(history_id) as id FROM analysis_history').fetchone()[0]
        connection.close()
        return next_id

    def get_all_info(self, id):
        connection = self.get_connection()
        result = connection.execute('SELECT * FROM analysis_history WHERE history_id = ?', (id,)).fetchone()
        connection.close()
        return result