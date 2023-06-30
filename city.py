from settings import INITIAL_CITY_MOTIF, FULL_PORTION, END_COLOR

class City():

    def __init__(self, country, color) -> None:
        self.country = country
        self.color = color
        self.motif = {
            country: INITIAL_CITY_MOTIF
        }

    def __str__(self) -> str:
        return f"{self.color}*{END_COLOR}"

    def transfer(self, city):
        if city is None:
            return
        for country in self.motif.keys():
            amount_to_transfer = self.motif[country] // FULL_PORTION
            if country in city.motif.keys():
                city.motif[country] += amount_to_transfer
            elif amount_to_transfer > 0: 
                city.motif[country] = amount_to_transfer
            self.motif[country] -= amount_to_transfer
    
    def is_complete(self, countries_list):
        return set(self.motif.keys()) == set(countries_list)