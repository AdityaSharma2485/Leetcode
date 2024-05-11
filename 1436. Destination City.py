from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start_cities = set()
        all_cities = set()

        # Extract all starting cities and all cities
        for path in paths:
            start_cities.add(path[0])
            all_cities.update(path)

        # Find the destination city
        for city in all_cities:
            if city not in start_cities:
                return city
