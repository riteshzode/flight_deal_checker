import requests
from flight_data import FlightData

#############################################################

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "TEQUILA_API_KEY"

flight_code_updated_url = f"{TEQUILA_ENDPOINT}/locations/query"

flight_search_url = f"{TEQUILA_ENDPOINT}/v2/search"

headers = {"apikey": TEQUILA_API_KEY}

#############################################################


class FlightSearch:

    def __init__(self):
        pass

    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        params1 = {
            "term": city_name,
            "location_types": "city"
        }
        r1 = requests.get(url=flight_code_updated_url, headers=headers, params=params1)
        code = r1.json()["locations"][0]["code"]
        return code

    def check_flight(self, origin_city_code, destination_city_code, date_from, date_to):
        params2 = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        r2 = requests.get(url=flight_search_url, headers=headers, params=params2)

        try:
            data = r2.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        else:

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: ${flight_data.price}")
            return flight_data