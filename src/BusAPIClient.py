import requests

class BusAPIClient:
    BASE_URL = "https://www.pamukkale.com.tr/yolcumneredeajax.php?islem=yolcum-nerede-sefer-kor&plaka={}"

    @classmethod
    def get_coordinates(cls, plaka):
        url = cls.BASE_URL.format(plaka.replace(" ", "%20"))
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            
            location = data.get("Location")
            latitude = data.get("Latitude")
            longitude = data.get("Longtitude") # NOTE: The external service has a typo in their response. They use "Longtitude" instead of the correct "Longitude".

            return location, latitude, longitude
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None

plaka_info = "35 PK 132"
location, latitude, longitude = BusAPIClient.get_coordinates(plaka_info)
print(f"Latitude: {latitude}, Longitude: {longitude}, Location: {location}")
