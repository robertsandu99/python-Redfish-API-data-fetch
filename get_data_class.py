import requests

class Fan:
    def __init__(self, base_url):
        self.url = base_url

    def get_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error trying to fetch data")

    def get_speeds(self):
        try:
            data = self.get_data()
            fan_1 = data["FanSpeedsPercent"][0]["SpeedRPM"]
            fan_2 = data["FanSpeedsPercent"][1]["SpeedRPM"]
            return fan_1, fan_2
        except Exception:
            raise Exception(f"Error while parsing the the data")
    
    def get_name(self):
        try:
            data = self.get_data()
            fan_1 = data["FanSpeedsPercent"][0]["DeviceName"]
            fan_2 = data["FanSpeedsPercent"][1]["DeviceName"]
            return fan_1, fan_2
        except Exception:
            raise Exception(f"Error while parsing the the data")

    def get_id(self):
        try:
            data = self.get_data()
            fan_1 = data["FanSpeedsPercent"][0]["DeviceId"]
            fan_2 = data["FanSpeedsPercent"][1]["DeviceId"]
            return fan_1, fan_2
        except Exception:
            raise Exception(f"Error while parsing the the data")
        
fan = Fan("http://localhost:8000/redfish/v1/Chassis/1/Sensor/Fan")

while True:
    x = int(input("input: "))
    if x == 1:
        print(fan.get_speeds())
    elif x == 2:
        print(fan.get_name())
    elif x == 3:
        print(fan.get_id())
    else:
        break
