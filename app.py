import json
import os
from http import HTTPStatus

from bson import ObjectId, json_util
from flask import Flask, request
from flask_pymongo import PyMongo

MONGODB_URI = os.environ.get('MONGODB_ENDPOINT')

app = Flask(__name__)
app.config['MONGO_URI'] = MONGODB_URI
mongo = PyMongo(app)


def parse_json(data):
    return json.loads(json_util.dumps(data))


@app.route('/items', methods=['GET'])
def get_all_items():
    items = list(mongo.db.items.find())
    return parse_json(items), HTTPStatus.OK


@app.route('/items', methods=['POST'])
def create_item():
    item = request.get_json()
    inserted_item = mongo.db.items.insert_one(item)
    return parse_json(inserted_item.inserted_id), HTTPStatus.CREATED


@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    item = mongo.db.items.find_one_or_404({'_id': ObjectId(item_id)})
    return parse_json(item), HTTPStatus.OK


@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    item = request.get_json()
    item_id_obj = ObjectId(item_id)
    result = mongo.db.items.update_one({'_id': item_id_obj}, {'$set': item})

    if result.matched_count == 0:
        return parse_json({'error': 'Item not found'}), HTTPStatus.NOT_FOUND

    updated_item = mongo.db.items.find_one({'_id': item_id_obj})
    return (
        parse_json(
            {'message': 'Item updated successfully', 'item': updated_item},
        ),
        HTTPStatus.OK,
    )


if __name__ == '__main__':
    app.run()
