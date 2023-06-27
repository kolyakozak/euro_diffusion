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

    def run_transfer(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] is not None:
                    if y - 1 >= 0:
                        self.grid[y][x].transfer(self.grid[y-1][x])
                    if y + 1 < self.height:
                        self.grid[y][x].transfer(self.grid[y+1][x])
                    if x - 1 >= 0:
                        self.grid[y][x].transfer(self.grid[y][x-1])
                    if x + 1 < self.width:
                        self.grid[y][x].transfer(self.grid[y][x+1])
