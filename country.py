

class Country():

    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color
        self.cities = []
        self.is_complete = False
        self.days_to_complete = 0

    def append_city(self, city):
        self.cities.append(city)

    def update_completenes_status(self, days, countries_list):
        if self.is_complete:
            return
        else:
            country_is_complete = True
            for city in self.cities:
                if city.is_complete(countries_list) == False:
                    country_is_complete = False
                    break
                else:
                    continue
            if country_is_complete:
                self.is_complete = True
                self.days_to_complete = days