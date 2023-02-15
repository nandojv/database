import pymongo
connessione = pymongo.MongoClient("mongodb://localhost:27017/")
nuovodatabase = connessione["griffin"]
nuovacollection = nuovodatabase["personaggi"]
# Definizione della lista
lista = [
  { "nome": "Lois", "cognome": "Griffin" },
  { "nome": "Stewie", "cognome": "Griffin" },
  { "nome": "Meg", "cognome": "Griffin" },
  { "nome": "Chris", "cognome": "Griffin" },
  { "nome": "Brian", "cognome": "Griffin" }
]
# Inserimento dei documenti
inserimento = nuovacollection.insert_many(lista)
print(inserimento.inserted_ids)

# Estrazione dei documenti di una collection
for selezione in nuovacollection.find():
  print(selezione)
  #selezione del primo documento della selezione
  selezione=nuovacollection.find_one()
  print(selezione)
