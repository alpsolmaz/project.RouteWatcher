import requests

class BusAPIClient:
    BASE_URL = "https://www.pamukkale.com.tr/yolcumneredeajax.php?islem=yolcum-nerede-sefer-kor&plaka={}"

    @classmethod
    def get_coordinates(cls, plaka):
        url = cls.BASE_URL.format(plaka.replace(" ", "%20"))

        try:
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()

            if not isinstance(data, dict) or not all(key in data for key in ["Location", "Latitude", "Longtitude"]):
                raise Exception("Received unexpected data structure from the API.")
            
            location = data["Location"]
            latitude = data["Latitude"]
            longitude = data["Longtitude"]  # Typo in the external service.
            
            return location, latitude, longitude
        
        except requests.RequestException as e:
            raise Exception(f"API Request Error: {str(e)}")
        except Exception as e:
            raise Exception(str(e))
