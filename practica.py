import json
import  requests
url = 'https://reqres.in/api/users/'
response = requests.get(url)
print(type(response))
print(response.status_code)
print(response.text)
json_data = response.json()
print(json_data)
print(json.dumps(json_data, indent=4))