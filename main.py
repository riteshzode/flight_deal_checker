# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import datetime
from data_manager import DataManager
from flight_search import FlightSearch

#############################################################
ORIGIN_CITY_IATA = "LON"
#############################################################

data_manager = DataManager()
flight_search = FlightSearch()

dict = data_manager.dict_create()

#############################################################
#############################################################

if dict[0]["iataCode"] == "":

    for i in dict:
        i["iataCode"] = flight_search.get_destination_code(i["city"])

    data_manager.dict = dict
    data_manager.update()

tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)

six_month_from_today = datetime.datetime.now() + datetime.timedelta(days=(6 * 30))


#############################################################
#############################################################

for data in dict:
    flight = flight_search.check_flight(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=data["iataCode"],
        date_from=tomorrow,
        date_to=six_month_from_today)
    print(f"lowest_price: ${data['lowestPrice']}\n")

    #############################################################
    #############################################################


    if flight is None:
        continue

    #############################################################
    #############################################################

    if flight.price <= data['lowestPrice']:


        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        ######################
        print(message)
        #######################

        # # just send this message on email
        # for email in emails:
        #     notification_manager.send_emails(emails=email, message=message)