import time
from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    while True:
        try:
            conn = mysql.connector.connect(
                host='db',  # Nome do serviço no docker-compose
                database='rh',
                user='root',
                password='root'
            )
            if conn.is_connected():
                return conn
        except Error as e:
            print(f"Error: {e}. Retrying...")
            time.sleep(2)  # Espera 2 segundos antes de tentar novamente

@app.route('/')
def index():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Failed to connect to the database"}), 500

    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
