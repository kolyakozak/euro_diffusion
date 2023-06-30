from city import City
from country import Country
from typing import List
from settings import COLORS

class Map():

    def __init__(self, countries, max_x, max_y) -> None:
        self.days = 0
        self.countries = []
        self.countries_names = []
        self.width = max_x
        self.height = max_y
        self.grid: List[List[str]] = [[None] * self.width for i in range(self.height)]
        for idx, country_info in enumerate(countries):
            country = Country(country_info[0], COLORS[idx])
            self.countries.append(country)
            self.countries_names.append(country_info[0])
            for y in range(country_info[2], country_info[4] + 1):
                for x in range(country_info[1], country_info[3] + 1):
                    city = City(country_info[0], COLORS[idx])
                    self.grid[y][x] = city
                    country.append_city(city)

    def display(self):
        for y in range(self.height - 1, -1, -1):
            for x in range(self.width):
                if self.grid[y][x] is not None:
                    print(self.grid[y][x], end=" ")
                else: 
                    print(" ", end=" ")
            print("\n")
    
    def run_diffusion(self):
        all_complete = self.all_complete()
        while not all_complete:
            self.run_transfer()
            self.days += 1
            all_complete = self.all_complete()

        return self.countries
    
    def all_complete(self):
        all_complete = True
        for country in self.countries:
            country.update_completenes_status(self.days, self.countries_names)
            if not country.is_complete:
                all_complete = False
        return all_complete
    
    def transfer_between_cities(self, city_from_x, city_from_y, city_to_x, city_to_y):
        if self.grid[city_from_y][city_from_x] is not None:
            if city_to_y >= 0 and city_to_y < self.height \
            and city_to_x >= 0 and city_to_x < self.width:
                self.grid[city_from_y][city_from_x].transfer(self.grid[city_to_y][city_to_x])

    def run_transfer(self):
        for y in range(self.height):
            for x in range(self.width):
                self.transfer_between_cities(x, y, x, y-1)
                self.transfer_between_cities(x, y, x, y+1)
                self.transfer_between_cities(x, y, x-1, y)
                self.transfer_between_cities(x, y, x+1, y)
