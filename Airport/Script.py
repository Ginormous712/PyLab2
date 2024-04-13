from Airport.Airport import Airport

url = "localhost"
user = "root"
password = "Password123"

airport = Airport(url, user, password)
print("Airport is connected")
print()

# Printing our tables i db Airport
airport.show_airlines()
print()
airport.show_flights()
print()

# Flights in airline 1
airport.show_flights_for_airline(1)
print()

# Adding flight and airline
airport.add_flight(6,3, "BERLIN", '2024-04-15 15:25:00', '2024-04-15 18:00:00')
airport.add_airline(4, "BNC")
airport.show_airlines()
print()
airport.show_flights()
print()

# Changing flight and airline
airport.change_airline(4, "WWW")
airport.change_flight(6, 1, 'MOSCOW', '2024-04-15 18:00:00', '2024-04-15 18:00:00')
airport.show_airlines()
print()
airport.show_flights()
print()

# Deleting flight and airline
airport.delete_flight(6)
airport.delete_airline(4)
airport.show_airlines()
print()
airport.show_flights()
print()

# Searching flight and airline by IDs
airport.search_airline(1)
print()
airport.search_flight(1)
print()