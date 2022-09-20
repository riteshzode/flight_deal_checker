import requests

#############################################################
sheet_url = "https://api.sheety.co/dc4ac9d78bc7736fb74d8eb42cadedb3/flightDeals/prices"
#############################################################


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.dict_create()

    def dict_create(self):
        r1 = requests.get(url=sheet_url)

        self.dict = r1.json()["prices"]

        return self.dict

    def update(self):
        for i in self.dict:
            data = {
                "price":
                    {
                        "city": i["city"],
                        "iataCode": i["iataCode"],
                        "lowestPrice": i["lowestPrice"],
                        "id": i["id"]

                    }
            }

            r2 = requests.put(
                url=f"https://api.sheety.co/dc4ac9d78bc7736fb74d8eb42cadedb3/flightDeals/prices/{i['id']}", json=data)

            print(r2.text)
