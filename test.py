# import requests
#
# api_url = 'http://localhost:8000/albom'
#
# data = requests.get(api_url).json()
# print(data)

data = {
    "id": 5,
    "title": "fiom3reiogtrjei9ogjre",
    "price": 4565
}

if data.get("id"):
    print(data['id'])

else:
    print("Error")