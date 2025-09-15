import requests

# 🔑 Replace with your actual Google Maps API key
API_KEY = "AIzaSyAAPjQ29toqdqWNvUCh9L1xSCFpFeRSFHg"

# Example address to geocode
address = "1600 Amphitheatre Parkway, Mountain View, CA"

url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"

response = requests.get(url)
data = response.json()

print("Status:", data["status"])
if data["status"] == "OK":
    location = data["results"][0]["geometry"]["location"]
    print("Latitude:", location["lat"])
    print("Longitude:", location["lng"])
else:
    print("Error:", data)
