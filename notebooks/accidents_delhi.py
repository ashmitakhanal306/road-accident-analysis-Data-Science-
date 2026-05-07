import pandas as pd
import numpy as np
import random

np.random.seed(42)

n = 400

dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="D")

locations = [
    "Connaught Place", "Karol Bagh", "Rohini",
    "Saket", "Dwarka", "Lajpat Nagar", "Chandni Chowk"
]

weather_types = ["Clear", "Rainy", "Foggy", "Cloudy"]
severity_levels = ["Minor", "Major", "Fatal"]

data = []

for i in range(n):
    date = pd.Timestamp(np.random.choice(dates))
    
    hour = np.random.randint(0, 24)
    minute = np.random.randint(0, 60)
    time = f"{hour:02d}:{minute:02d}"
    
    location = random.choice(locations)
    weather = np.random.choice(weather_types, p=[0.5, 0.2, 0.15, 0.15])
    
    vehicles = np.random.randint(1, 5)
    
    if weather in ["Rainy", "Foggy"] and (hour >= 18 or hour <= 5):
        severity = np.random.choice(severity_levels, p=[0.4, 0.4, 0.2])
    else:
        severity = np.random.choice(severity_levels, p=[0.7, 0.25, 0.05])
    
    if severity == "Minor":
        casualties = np.random.randint(0, 2)
    elif severity == "Major":
        casualties = np.random.randint(1, 4)
    else:
        casualties = np.random.randint(2, 6)
    
    temperature = np.random.randint(5, 45)
    
    data.append([
        i+1, date.strftime("%Y-%m-%d"), time, location, weather,
        vehicles, severity, casualties, temperature
    ])

# CREATE DATAFRAME (THIS WAS MISSING ❗)
df = pd.DataFrame(data, columns=[
    "ID", "Date", "Time", "Location", "Weather",
    "Vehicles_Involved", "Accident_Severity",
    "Casualties", "Temperature"
])

# NOW SAVE CSV
df.to_csv("accidents_delhi.csv", index=False)

print("Dataset created successfully!")