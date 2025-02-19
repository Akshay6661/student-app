from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os


# Load .env file
load_dotenv()

# Get the environment variable
mongo_uri = os.getenv('MONGO_URI')

## create a new client and connect to the server 
client = MongoClient(mongo_uri, server_api=ServerApi('1'))


## send a ping to confirm a successful connection 
try:
    client.admin.command('ping')
    print('Connected to MongoDB')
except Exception as e:
    print('Failed to connect to MongoDB', str(e))