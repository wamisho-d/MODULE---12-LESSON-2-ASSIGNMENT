from flask import Flask, jsonify, request
from mysql.connector import connect, Error
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)

# Database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_user'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DATABASE'] = 'your_database'

# Database connection setup
def get_db_connection():
    try:
        connection = connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DATABASE']
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None