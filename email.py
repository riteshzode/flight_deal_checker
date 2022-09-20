import requests

url = "https://api.sheety.co/59b19d45b08c1164ac47aa206c081b90/flightDeals/users"

data = {
    "user":
        {
            "firstName": "rahul",
            "lastName": "panday",
            "email": "abcxyz@gmail.com"

        }

}

r1 = requests.post(url=url, json=data)
print(r1.text)

# r1 = requests.delete(url="https://api.sheety.co/59b19d45b08c1164ac47aa206c081b90/flightDeals/users/3")
# print(r1.text)
