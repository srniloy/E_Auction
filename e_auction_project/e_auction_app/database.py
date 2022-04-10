import djongo

print(djongo.__version__)
# DB_URL = 'mongodb+srv://Instraverse:instraverse11@cluster0.tng4e.mongodb.net/myFirstDatabase?authSource=admin&replicaSet=atlas-h4pkce-shard-0&w=majority&readPreference=primary&retryWrites=true&ssl=true'

# try:
#     my_client = pymongo.MongoClient(DB_URL)
# except Exception:
#     print('error')


# # First define the database name
# dbname = my_client['E_Auction']

# # Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection
# collection_name = dbname["userinfo"]
# medicine_1 = {
#     "medicine_id": "RR000123456",
#     "common_name": "Paracetamol",
#     "scientific_name": "",
#     "available": "Y",
#     "category": "fever"
# }
# medicine_2 = {
#     "medicine_id": "RR000342522",
#     "common_name": "Metformin",
#     "scientific_name": "",
#     "available": "Y",
#     "category": "type 2 diabetes"
# }
# # Insert the documents
# collection_name.insert_many([medicine_1, medicine_2])
