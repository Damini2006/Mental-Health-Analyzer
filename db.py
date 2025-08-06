
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mental_health"]
collection = db["chat_logs"]

def save_chat(user, user_msg, bot_msg, mood):
    collection.insert_one({
        "user": user,
        "user_msg": user_msg,
        "bot_msg": bot_msg,
        "mood": mood
    })

def get_user_history(user):
    return list(collection.find({"user": user}))
