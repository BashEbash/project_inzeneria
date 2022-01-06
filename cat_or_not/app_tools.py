import os
import sqlite3
from re import split

from flask import flash
from werkzeug.utils import redirect


def save_folder_exists(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

def file_size(file):
    file.seek(0, os.SEEK_END)
    file_size = file.tell()
    file.seek(0)
    return file_size

def get_connection():
    return sqlite3.connect('database.db')

def add_result(filename):
    conn = get_connection()
    conn.execute("INSERT INTO results (file_name) VALUES (?)", (filename,))
    conn.commit()
    conn.close()

def get_result(id):
    conn = get_connection()
    result = conn.execute('SELECT file_name FROM results WHERE id = ?', (id,)).fetchone()[0]
    conn.close()
    return result

def get_max_id():
    conn = get_connection()
    next_id = conn.execute('SELECT MAX(id) as id FROM results').fetchone()[0]
    conn.close()
    return next_id




