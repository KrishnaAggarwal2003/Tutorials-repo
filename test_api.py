## Testing the API
from flask import Flask, request, jsonify
import pytest

app = Flask(__name__)

# Simulated database (in memory)
users = {}

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({"id": user_id, "name": user}),200

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    user_id = data.get("id")
    name = data.get("name")
    
    if not user_id or not name:
        return jsonify({'error': 'Please provide id and name'}), 400
    if user_id in users:
        return jsonify({'error': 'User already exists'}), 400
    users[user_id] = name
    return jsonify({"id": user_id, "name": name}), 201
    

## Testing
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client # Provide the test client instance
        
def test_add_user(client):
    response = client.post('/users', json={"id": 1, "name": "Alice"})
    assert response.status_code == 201
    assert response.json == {"id": 1, "name": "Alice"}
 
def test_get_user(client):
    client.post('/users', json={"id": 2, "name": "John"})
    response = client.get('/users/2')
    assert response.status_code == 200
    assert response.json == {"id": 2, "name": "John"}                 