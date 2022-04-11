import pymongo
from .models import *

DB_URL = 'mongodb+srv://Instraverse:instraverse121@cluster0.tng4e.mongodb.net/myFirstDatabase?authSource=admin&replicaSet=atlas-h4pkce-shard-0&w=majority&readPreference=primary&retryWrites=true&ssl=true'


my_client = pymongo.MongoClient(DB_URL)

dbname = my_client['eAuction']

collection_name = dbname["userinfo"]
product_coll = dbname["product_info"]


def store_user_info(email):
    user_info = UserInformation()
    user_info.set_values(collection_name.count_documents({}), email)
    collection_name.insert_one(user_info.get_values())
    print(user_info.get_values())


def verify_user_email(email):
    result = collection_name.find_one({"email": email})
    if result:
        return True
    else:
        return False


def store_product_info(data):
    product_detail = ProductDetails()
    product_detail.set_value(data['user_email'], data['name'], data['detail'], data['price'], data['dtime'])
    product_coll.insert_one(product_detail.get_value())


def get_all_product():
    # data = dict(product_coll.find())
    return product_coll.find()


def get_all_product_by_email(email):
    return product_coll.find({"user_email": email})
