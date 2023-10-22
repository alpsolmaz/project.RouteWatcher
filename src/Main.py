from BusAPIClient import BusAPIClient
import time

class BusTrackerCLI:

    def __init__(self):
        self.plate = ""
        self.interval = None

    def prompt_plate(self):
        self.plate = input("Lütfen plaka bilgisini giriniz: ")

    def fetch_coordinates(self):
        if not self.plate:
            print("Önce plaka bilgisini girmelisiniz.")
            return

        try:
            location, latitude, longitude = BusAPIClient.get_coordinates(self.plate)
            print(f"Latitude: {latitude}, Longitude: {longitude}, Location: {location}")
        except Exception as e:
            print(e)

    def set_interval(self, minutes):
        self.interval = minutes * 60

    def start(self):
        while True:
            command = input("Komut giriniz (where, where set [dakika], exit): ")
            
            if command == "where":
                self.fetch_coordinates()
            elif "where set" in command:
                try:
                    minutes = int(command.split()[-1])
                    self.set_interval(minutes)
                    print(f"Her {minutes} dakikada bir otomatik sorgulama başlatıldı.")
                    while self.interval:
                        time.sleep(self.interval)
                        self.fetch_coordinates()
                except ValueError:
                    print("Lütfen geçerli bir dakika değeri girin.")
            elif command == "exit":
                break

if __name__ == "__main__":
    cli = BusTrackerCLI()
    cli.prompt_plate()
    cli.start()
