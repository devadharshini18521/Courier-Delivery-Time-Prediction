import pandas as pd
import random

pickup_locations = [
    "Chennai", "Mumbai", "Delhi", "Bangalore",
    "Hyderabad", "Pune", "Kolkata", "Ahmedabad"
]

destinations = [
    "Chennai", "Mumbai", "Delhi", "Bangalore",
    "Hyderabad", "Pune", "Kolkata", "Ahmedabad"
]

courier_types = [
    "Standard",
    "Express",
    "Same Day"
]

data = []

for i in range(10000):

    pickup = random.choice(pickup_locations)
    destination = random.choice(destinations)
    courier = random.choice(courier_types)

    historical = random.randint(1, 7)

    # Generate realistic delivery days
    actual = historical + random.choice([-1, 0, 1])

    if actual < 1:
        actual = 1

    data.append([
        pickup,
        destination,
        courier,
        historical,
        actual
    ])

df = pd.DataFrame(data, columns=[
    "Pickup_Location",
    "Destination",
    "Courier_Type",
    "Historical_Deliveries",
    "Actual_Delivery_Days"
])

df.to_csv("Courier_Delivery_Dataset.csv", index=False)

print("Dataset created successfully!")