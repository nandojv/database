import pymongo
connessione = pymongo.MongoClient("mongodb://localhost:27017/")
nuovodatabase = connessione["griffin"]
nuovacollection = nuovodatabase["personaggi"]
# Definizione del dizionario
dizionario = { "nome": "Peter", "cognome": "Griffin" }
dizionario = { "nome": "cane", "cognome": "Griffin" }
# Inserimento del documento
inserimento = nuovacollection.insert_one(dizionario)
print(inserimento.inserted_id)
print(connessione.list_database_names())
