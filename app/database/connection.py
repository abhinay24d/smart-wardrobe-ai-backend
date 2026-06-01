from pymongo import MongoClient

MONGO_URL = "mongodb+srv://abhinay:abhinay123@smart-wardrobe-cluster.ljuejtv.mongodb.net/?retryWrites=true&w=majority&appName=smart-wardrobe-cluster"

client = MongoClient(MONGO_URL)

db = client["smart_wardrobe_ai"]