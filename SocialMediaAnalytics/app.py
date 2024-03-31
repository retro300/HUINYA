poetry add flask==3.0.0 pandas gpt3discord
from flask import Flask, jsonify, request
from models import Post
from controller import DataController

app = Flask(__name__)

# Здесь будет храниться список всех постов (в реальном приложении это будет база данных)
posts = []

@app.route('/add_post', methods=['POST'])
def add_post():
    data = request.json
    post = Post(**data)
    posts.append(post)
    return jsonify({'message': 'Post added successfully!'}), 201

@app.route('/aggregate_data', methods=['GET'])
def aggregate_data():
    controller = DataController(posts)
    result = controller.aggregate_data()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)