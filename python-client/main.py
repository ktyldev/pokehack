import requests
import http.client
import json

# Get info from Pokeapi
req = requests.get('https://pokeapi.co/api/v2/pokemon/1/')
print("server responded with " + str(req.status_code))
<<<<<<< HEAD
  
=======

>>>>>>> 8ea00af12994dd0c47a481733ba18b77b5839356
print ("deserializing data... ", end="")
json_response = json.loads(req.content)
print("done!")

print("loaded " + json_response['name'] + "'s data.")

# Payload to send necessary data to game server
payload = {
<<<<<<< HEAD
    "id": json_response['id'], 
=======
    "id": json_response['id'],
>>>>>>> 8ea00af12994dd0c47a481733ba18b77b5839356
    "name": json_response['name'],
    "moves": json_response['moves']
}

# Join request to game server
req = requests.post('http://192.168.69.1:42069/joinson', json.dumps(payload))
