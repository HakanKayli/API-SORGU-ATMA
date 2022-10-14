import requests


response = requests.get("https://dog.ceo/api/breeds/image/random")
print(response.json())

print("\n")

response2 = requests.get("https://api.catboys.com/img")
print(response2.json())

print("\n")

response3 = requests.get("https://jsonplaceholder.typicode.com/users/8")
print(response3.json())

