import requests
import time
    

def retrieve_power_usage():
    try:
        response = requests.get("http://localhost:8000/redfish/v1/Chassis/1/Power")
        if response.status_code == 200:
            data = response.json()
            try:
                power_usage = data["PowerSupplies"][0]["LastPowerOutputWatts"]
                print(f"\nLast power usage is: {power_usage}W")
            except Exception:
                 print("Error while parsing data, data format has changed")
        else:
            print("Can not fetch data, something is wrong")
    except Exception:
            print("Server is down, come back later")


def retrieve_fan_speed():
    try:
        response = requests.get("http://localhost:8000/redfish/v1/Chassis/1/Sensor/Fan")
        if response.status_code == 200:
            data = response.json()
            try:
                fan_speed_1 = data["FanSpeedsPercent"][0]["SpeedRPM"]
                fan_speed_2 = data["FanSpeedsPercent"][1]["SpeedRPM"]
                print(f"\nFan speeds are:\nFan 1: {fan_speed_1} RPM\nFan 1: {fan_speed_2} RPM")
            except Exception:
                 print("Error while parsing data, data format has changed")
        else:
            print("Can not fetch data, something is wrong")
    except Exception:
            print("Server is down, come back later")


def retrieve_cpu_temp():
    try:
        response = requests.get("http://localhost:8000/redfish/v1/Chassis/1/Thermal/CPU")

        if response.status_code == 200:
            data = response.json()
            try:
                cpu_temp = data['Reading']
                cpu_temp_unit = data["ReadingUnits"]
                print(f"\nCpu temp is: {cpu_temp} {cpu_temp_unit}")
            except Exception:
                 print("Error while parsing data, data format has changed")            
        else:
            print("Can not fetch data, something is wrong")
    except Exception:
            print("Server is down, come back later")


def retrieve_memory_temp():
    try:
        response = requests.get("http://localhost:8000/redfish/v1/Chassis/1/Thermal/Memory")
        if response.status_code == 200:
            data = response.json()
            try:
                memory_temp= data['Reading']
                memory_temp_unit = data["ReadingUnits"]
                print(f"\nMemory temp is: {memory_temp} {memory_temp_unit}")
            except Exception:
                 print("Error while parsing data, data format has changed")
        else:
            print("Can not fetch data, something is wrong")
    except Exception:
            print("Server is down, come back later")


while True:
    try:
        select_option = int(input("\n======== Select what script you want to use ========\n" \
        "Insert 1 for PSU power usage\n" \
        "Insert 2 to retrieve fan speeds\n" \
        "Insert 3 to obtain temperature reading for CPU\n" \
        "Insert 4 to obtain temperature reading for memory\n" \
        "Insert 5 to exit\n" \
        "--> "))
        if select_option == 1:
            retrieve_power_usage()
        elif select_option == 2:
            retrieve_fan_speed()
        elif select_option == 3:
            retrieve_cpu_temp()
        elif select_option == 4:
            retrieve_memory_temp()
        elif select_option == 5:
            print("exitign...")
            break
        else:
            print("\nNo script available for this number")
        time.sleep(3)
    except ValueError:
        print("\nPlease insert a digit/numbar")
        time.sleep(3)
    except Exception as e:
        print(f"\n@@@@@@@ {e}")
        time.sleep(3)
