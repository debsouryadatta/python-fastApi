from pymongo import MongoClient
MONGO_URI = "mongodb+srv://Neel:lovecoding@cluster0.qymvclt.mongodb.net/fastapi_cwh?retryWrites=true&w=majority&appName=Cluster0"

conn = MongoClient(MONGO_URI)