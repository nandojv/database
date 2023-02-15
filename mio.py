import pymongo
# Connessione a MongoDB
connessione = pymongo.MongoClient('mongodb://localhost:27017/')
# Stampa a video della lista dei database



print(connessione.list_database_names())