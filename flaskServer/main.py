import json

from flask import Flask, jsonify, request

from flask_cors import CORS, cross_origin


import mysql.connector

env = open('./flaskServer/env.json')
data = json.load(env)


# Connect to MySQL

mydb = mysql.connector.connect(
    host=data['host'],
    port=data['port'],
    user=data['user'],
    password=data['password'],
    database=data['database']
)

#create table
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS emails (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")



def create_app():
    app = Flask(__name__)
    CORS(app)
    @app.route('/', methods=['GET'])
    def index():
        return jsonify({'message': 'Hello World!'})
    

    @app.route('/api', methods=['POST'])
    def api():
        data = request.get_json()
        return jsonify(data)

    @app.route('/api/<name>', methods=['GET'])
    def api_name(name):
        if name == 'hello':
            return jsonify({'message': 'Hello World!'})
        else:
            return jsonify({'message': name + ' ' + 'is not a valid endpoint.'})
    
    @app.route('/api/add_template', methods=['POST'])
    @cross_origin()
    def add_template():
        data = request.get_json()
        sql = "INSERT INTO emails (name, subject, body) VALUES (%s, %s)"
        val = (data['name'], data['subject'], data['body'])
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({'message': 'Template added!'})


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

    