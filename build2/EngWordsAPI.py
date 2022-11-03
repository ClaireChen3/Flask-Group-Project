import requests

url = "https://wft-geo-db.p.rapidapi.com/v1/geo/adminDivisions"

headers = {
	"X-RapidAPI-Key": "2589d0d945msh900743935f389a8p15c96ejsn5364cd142d31",
	"X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

# print(response.text)

print("City Data: Al Mamzar")
cities = response.json().get('data')
for city in cities:  # countries is a list
    if city["name"] == "Al Mamzar":  # this filters for USA
        for key, value in city.items():  # this finds key, value pairs in country
            print(key, value)