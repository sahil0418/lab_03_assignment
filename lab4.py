# Define the flight data as a list of dictionaries
flight_data = [
    {"Flight ID": "AI161E90", "From": "BLR", "To": "BOM", "Price": 5600},
    {"Flight ID": "BR161F91", "From": "BOM", "To": "BBI", "Price": 6750},
    {"Flight ID": "AI161F99", "From": "BBI", "To": "BLR", "Price": 8210},
    {"Flight ID": "VS171E20", "From": "JLR", "To": "BBI", "Price": 5500},
    {"Flight ID": "AS171G30", "From": "HYD", "To": "JLR", "Price": 4400},
    {"Flight ID": "AI131F49", "From": "HYD", "To": "BOM", "Price": 3499},
]

# City codes and their corresponding names
city_names = {
    "BLR": "Bengaluru",
    "BOM": "Mumbai",
    "BBI": "Bhubaneswar",
    "HYD": "Hyderabad",
    "JLR": "Jabalpur",
}

# Function to search and print flight data based on user input
def search_flights():
    print("Search Options:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        city_code = input("Enter the city code to search for flights: ")
        city_name = city_names.get(city_code, "Unknown City")
        print(f"Flights to/from {city_name}:")
        for flight in flight_data:
            if flight["From"] == city_code or flight["To"] == city_code:
                print(f"Flight ID: {flight['Flight ID']}, From: {city_names[flight['From']]}, To: {city_names[flight['To']]}, Price: {flight['Price']}")
    
    elif choice == "2":
        city_code = input("Enter the city code to search for outbound flights: ")
        city_name = city_names.get(city_code, "Unknown City")
        print(f"Flights from {city_name}:")
        for flight in flight_data:
            if flight["From"] == city_code:
                print(f"Flight ID: {flight['Flight ID']}, To: {city_names[flight['To']]}, Price: {flight['Price']}")
    
    elif choice == "3":
        from_city_code = input("Enter the source city code: ")
        to_city_code = input("Enter the destination city code: ")
        from_city_name = city_names.get(from_city_code, "Unknown City")
        to_city_name = city_names.get(to_city_code, "Unknown City")
        print(f"Flights from {from_city_name} to {to_city_name}:")
        for flight in flight_data:
            if flight["From"] == from_city_code and flight["To"] == to_city_code:
                print(f"Flight ID: {flight['Flight ID']}, Price: {flight['Price']}")
    
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

# Main program loop
while True:
    search_flights()
    another_search = input("Do you want to perform another search? (yes/no): ")
    if another_search.lower() != "yes":
        break
