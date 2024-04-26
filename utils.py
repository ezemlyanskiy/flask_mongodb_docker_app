from bson import ObjectId
from bson.errors import InvalidId

from exceptions import ItemNotFoundError


def convert_item_id(item_id):
    try:
        object_id = ObjectId(item_id)
        return object_id
    except InvalidId:
        raise ItemNotFoundError
