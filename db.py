from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.o2cbi29.mongodb.net/Cluster0?retryWrites=true&w=majority',
                     UuidRepresentation="standard")
