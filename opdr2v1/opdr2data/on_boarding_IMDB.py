import pymongo
import requests
import json

# ophalen van de data
url = 'https://imdb-api.com/en/API/Top250Movies/k_1abwersp'
response = requests.get(url)
data = response.json()

# hiermee stel ik de data op de juiste manier op zodat hij leesbaar geprint kan worden

for movie in data['items']:
    title = movie['title']
    year = movie['year']
    rating = movie ['imDbRating']
    print(f'{title} ({year}) - Rating: {rating}')

# v2: Hiermee word er een verbinding gemaakt met een database die in een andere container draait met een mongo database
client = pymongo.MongoClient('mongodb://mongoadmin:bdung@mongo:27017/?authSource=admin')

db = client['mydatabase']

collection = db['mycollection']

# meerdere documenten toevoegen
result = collection.insert.many(data)
print(f'Inserted {len(result.inserted_ids)} documents')
