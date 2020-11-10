import requests, json
nombre_url= input('Introduce la url: ')
url = "https://reqres.in/api/users/"
response = requests.get(url)
# print(type(response))
# print(response.status_code)
# print(response.text)
json_data = response.json()
data_array = json_data["data"]
for item in data_array:
    print(f"Id: {item['id']} Name: {item['first_name']}")
# print(json.dumps(json_data, indent=4))
# print(data)
try:
    response = requests.get(nombre_url)
except requests.exceptions.ConnectionError as e:
    pass


