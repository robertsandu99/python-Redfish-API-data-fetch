from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import json


app = FastAPI()
'''

References

https://www.supermicro.com/manuals/other/redfish-ref-guide-html/Content/general-content/available-apis.htm

https://github.com/DMTF/Redfish-Mockup-Server/blob/main/public-rackmount1/Chassis/1U/Power/index.json

https://fastapi.tiangolo.com/#check-it

https://fastapi.tiangolo.com/advanced/response-directly/#using-the-jsonable_encoder-in-a-response

https://github.com/robertsandu99


'''


def read_json_file(file_path: str):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return None
    

@app.get("/redfish/v1/Chassis/1/Power")
async def get_power():
    power_data = read_json_file("power_usage.json")
    if power_data is None:
        raise HTTPException(status_code=404, detail="File not found")
    return JSONResponse(content=power_data)


@app.get("/redfish/v1/Chassis/1/Thermal/CPU")
async def get_cpu_temp():
    cpu_temp = read_json_file("cpu_temp.json")
    if cpu_temp is None:
        raise HTTPException(status_code=404, detail="File not found")
    return JSONResponse(content=cpu_temp)


@app.get("/redfish/v1/Chassis/1/Thermal/Memory")
async def get_memory_temp():
    memory_temp = read_json_file("memory_temp.json")
    if memory_temp is None:
        raise HTTPException(status_code=404, detail="File not found")
    return JSONResponse(content=memory_temp)


@app.get("/redfish/v1/Chassis/1/Sensor/Fan")
async def get_fan_speed():
    fan_speed = read_json_file("fan_speed.json")
    if fan_speed is None:
        raise HTTPException(status_code=404, detail="File not found")
    return JSONResponse(content=fan_speed)
