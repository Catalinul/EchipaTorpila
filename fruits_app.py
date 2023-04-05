from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)


API_BASE_URL = 'https://fruityvice.com/api/fruit/all'
DATA_FILE_PATH = 'data.json'


@app.route('/liveness')
def liveness():
    return "hello dev school"


def fetch_data():
    response = requests.get(API_BASE_URL)# EchipaTorpila
    if response.status_code == 200:
        data = response.json()
        with open(DATA_FILE_PATH, 'w') as f:
            json.dump(data, f)
        return data
    else:
        return {}


@app.route('/fruit/', methods=['GET'])
def get_all_fruits():
    data = request.get_json()
    try:
        with open(DATA_FILE_PATH, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = fetch_data()
    return jsonify(data)


@app.route('/fruit/<int:id>', methods=['GET'])
def get_fruit_by_id(id):
    try:
        with open(DATA_FILE_PATH, 'r') as f:
            fruits = json.load(f)
    except FileNotFoundError:
        fruits = []

    for fruit in fruits:
        if fruit['id'] == id:
            return jsonify(fruit)
    return jsonify({'error': 'Fruit not found'})


@app.route('/fruit/', methods=['POST'])
def fruit():
    data = request.get_json()
    try:
        with open(DATA_FILE_PATH, 'r') as f:
            fruits = json.load(f)
    except FileNotFoundError:
        fruits = []

    data['id'] = len(fruits) + 1
    fruits.append(data)
    with open(DATA_FILE_PATH, 'w') as f:
        json.dump(fruits, f)
    return jsonify({'message': f'Fruit {len(fruits)+1} added successfully'})


@app.route('/fruit/<int:id>', methods=['PUT'])
def update_fruit(id):
    data = request.get_json()
    try:
        with open(DATA_FILE_PATH, 'r') as f:
            fruits = json.load(f)
    except FileNotFoundError:
        fruits = []
    
    try:
        [fruits.update(data) for fruit in fruits if fruit["id"] == id]
    except ValueError:
        return jsonify({'error': 'Fruit not found'})

    with open(DATA_FILE_PATH, 'w') as f:
        json.dump(fruits, f)
    return jsonify({'message': 'Fruit updated successfully'})


@app.route('/fruit/<int:id>', methods=['DELETE'])
def delete_fruit(id):
    try:
        with open(DATA_FILE_PATH, 'r') as f:
            fruits = json.load(f)
    except FileNotFoundError:
        fruits = []

    try:
        [fruits.remove(fruit) for fruit in fruits if fruit["id"] == id]
    except ValueError:
        return jsonify({'error': 'Fruit not found'})
	
    with open(DATA_FILE_PATH, 'w') as f:
        json.dump(fruits, f)
    return jsonify({'message': 'Fruit deleted successfully'})
    

if __name__ == '__main__':
    app.run(debug=True)
