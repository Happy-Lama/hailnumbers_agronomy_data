import requests
import json
import time
# Define the URL where the POST requests will be sent
url = 'http://localhost:8000/api/soilParameters/add/'

# Define the data to be sent in the POST request
data = {
    'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
    'soil_temperature': 25.5,
    'soil_moisture': 0.6,
    'soil_ph': 6.5,
    'soil_nitrogen_content': 0.2,
    'soil_phosphorus_content': 0.1,
    'soil_potassium_content': 0.3,
    'soil_electrical_conductivity': 0.5
}

# Send the POST request
response = requests.post(url, json=json.dumps(data))

# Check the response status
if response.status_code == 201:
    print("Soil parameters successfully created.")
else:
    print("Failed to create soil parameters. Status code:", response.status_code)
