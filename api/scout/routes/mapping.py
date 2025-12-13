import os
import json

import requests
from fastapi import APIRouter

router = APIRouter()


@router.post("")
async def add_location_to_scout(addr: str):
    address = ""
    for char in addr:
        if char == " ":
            address += "+"
        elif char == ",":
            address += "%2C"
        else:
            address += char

    # 5201 Woodward Ave, Detroit, MI 
    url = f"https://api.mapbox.com/search/geocode/v6/forward?q={address}&access_token=pk.eyJ1IjoiY2FsbGVuZW5naW5lZXJpbmciLCJhIjoiY21pdzd2NWs4MTZseTNjbmI3ZXVnNWhzOSJ9.0JIeAB9Pki4t5VQTZ_5zgg"
    
    res = requests.get(url).json()
    loc = res['features'][0]['properties']

    loc_json = json.dumps(loc, indent=4)
    with open('output.json', 'w') as f:
        f.write(loc_json)

    return loc_json