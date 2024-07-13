import datetime
import json
from typing import List, Dict, Any


class Weather:
    def __init__(self, data: List[Dict[str, Any]]):
        self.data = data

    def weather_data(self) -> str:
        results = []
        for i in self.data:
            timestamp = datetime.datetime.fromtimestamp(i['dt']).strftime('%Y-%m-%d %H:%M:%S')
            entry = {
                "timestamp": timestamp,
                "current": i['main']['temp'],
                "feels_like": i['main']['feels_like'],
                "max": i['main']['temp_max'],
                "min": i['main']['temp_min']
            }
            results.append(entry)

        return json.dumps(results, indent=4)



