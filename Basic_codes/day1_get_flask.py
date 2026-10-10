## normal get request
'''import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response.json())
print(response.status_code)'''


## using params in get request
import requests

url = "https://jsonplaceholder.typicode.com/users"

params = {
    "id": 1
}

response = requests.get(url, params=params)

print(response.url)
print(response.json())