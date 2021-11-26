def get_database():
  from pymongo import MongoClient
  import pymongo

  # Provide the mongodb atlas url to connect python to mongodb using pymongo
  CONNECTION_STRING = "mongodb+srv://blog:blog@cluster0.2grje.mongodb.net/myFirstDatabase"

  # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
  from pymongo import MongoClient
  client = MongoClient(CONNECTION_STRING)

  # Create the database for our examples
  return client['beers']
        
def insert_beer(beer):
  db = get_database()
  result = db.beers.insert_one(beer)
  return result

def get_beer(beer_id):
  db = get_database()
  result = db.beers.find_one({'_id': beer_id})
  return result

def get_all_beers():
  db = get_database()
  result = db.beers.find()
  return result

def edit_beer(beer_id, beer):
  db = get_database()
  result = db.beers.update_one({'_id': beer_id}, {'$set': beer})
  return result

def delete_beer(beer_id):
  db = get_database()
  result = db.beers.delete_one({'_id': beer_id})
  return result

def cleanup():
  db = get_database()
  db.beers.delete_many({})

# Get the database
dbname = get_database()

beer = {
  "_id": "1",
  "name": "Megalomania Mango IPA",
  "abv": 7.5,
  "is_tapped": True
}

beer_2 = {
  "_id": "2",
  "name": "Paranoid Porter",
  "abv": 4.8
}

beer_with_recipe = {
  "_id": "3",
  "name": "Narcoleptic NEIPA",
  "abv": 6.2,
  "is_tapped": True,
  "recipe": "Mash 60 minutes @ 152. Boil 60 minutes.",
  "grains": [
    {"malt": "2 row", "qty": 13, "unit": "lbs"},
    {"malt": "Marris Otter", "qty": 13, "unit": "lbs"},
    {"malt": "white wheat", "qty": 13, "unit": "lbs"},
    {"malt": "flaked oat", "qty": 4, "unit": "lbs"},
    {"malt": "honey", "qty": 2, "unit": "lbs"}
  ],
  "hops": [
    {"hop": "Citra", "qty": 4, "unit": "oz", "time": "Boil 5"},
    {"hop": "Simcoe", "qty": 4, "unit": "oz", "time": "Boil 5"},
    {"hop": "Mosaic", "qty": 4, "unit": "oz", "time": "Boil 5"},
    {"hop": "Citra", "qty": 4, "unit": "oz", "time": "Hold 30 @ 180"},
    {"hop": "Simcoe", "qty": 4, "unit": "oz", "time": "Hold 30 @ 180"},
    {"hop": "Mosaic", "qty": 4, "unit": "oz", "time": "Hold 30 @ 180"},
    {"hop": "Citra", "qty": 8, "unit": "oz", "time": "Dry Hop"},
    {"hop": "Simcoe", "qty": 8, "unit": "oz", "time": "Dry Hop"},
    {"hop": "Mosaic", "qty": 8, "unit": "oz", "time": "Dry Hop"}
  ],
  "yeast": [
    {"yeast": "US-05", "qty": 1, "unit": "packet"}
  ]
}

cleanup()


result = insert_beer(beer)
print("Inserted beer id: " + result.inserted_id)

print("Listing the beer that was just inserted")
print(get_beer(result.inserted_id))

print("Adding more beers")
result = insert_beer(beer_2)
result = insert_beer(beer_with_recipe)

print("Listing all beer names")
beers = get_all_beers()
for beer in beers :
  text = beer['name']
  if "is_tapped" in beer and beer["is_tapped"]:
    text = text + " -- AVAILABLE"
  print(text)
