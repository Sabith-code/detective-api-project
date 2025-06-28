from pymongo import MongoClient

# Connect to MongoDB (Default: localhost:27017)
client = MongoClient("mongodb://localhost:27017/")

# Use (or create) the detective database
db = client["detective_db"]

# Define collections
cases = db["cases"]
clues = db["clues"]
suspects = db["suspects"]
