def calculate_fare(distance):
    base_fare = 50  # Base fare in dollars
    distance_fare = 10  # Fare per kilometer in dollars
    total_fare = base_fare + (distance * distance_fare)
    return total_fare

trips = [5, 10, 3]  # Distances in kilometers

total_fare = 0

for i, distance in enumerate(trips, start=1):
    fare = calculate_fare(distance)
    total_fare += fare
    print(f"Trip {i}: ${fare}")

print(f"Total Fare: ${total_fare}")
