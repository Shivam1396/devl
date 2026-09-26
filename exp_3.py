import requests
import pandas as pd
import matplotlib.pyplot as plt
city = "Pune"
latitude = 18.5204
longitude = 73.8567
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": latitude,
    "longitude": longitude,
    "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    "timezone": "Asia/Kolkata",
    "forecast_days": 7
}
response = requests.get(url, params=params)
data = response.json()
print("API DATA:")
print(data)
df = pd.DataFrame({
    "Date": data["daily"]["time"],
    "Max Temperature": data["daily"]["temperature_2m_max"],
    "Min Temperature": data["daily"]["temperature_2m_min"],
    "Rainfall": data["daily"]["precipitation_sum"]
})
print("\nWEATHER DATA:")
print(df)
print("\nMISSING VALUES:")
print(df.isnull().sum())
print("\nDATA TYPES:")
print(df.dtypes)
print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())
plt.plot(
    df["Date"],
    df["Max Temperature"],
    marker="o"
)
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Pune Temperature Forecast")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
