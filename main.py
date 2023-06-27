import sys
from map import Map
from settings import MAX_COUNTRIES, END_COLOR, INPUT_FILE
import logging

logger = logging.Logger(__name__)

input_file = open(INPUT_FILE, "r")
sys.stdin = input_file


def simulate_euro_coins():
    case_number = 1

    while True:
        num_countries = int(input())
        if num_countries == 0:
            break
        if num_countries > MAX_COUNTRIES:
            logger.error(f"To many countries, maximum countries number is {MAX_COUNTRIES}")
            break

        max_x = 0
        max_y = 0
        countries = []
        for _ in range(num_countries):
            country_info = input().split()
            country_name = country_info[0]
            xl, yl, xh, yh = map(lambda z: int(z) - 1, country_info[1:])
            max_x = max(max_x, xh + 1)
            max_y = max(max_y, yh + 1)
            countries.append((country_name, xl, yl, xh, yh))


        eu_map = Map(countries, max_x, max_y)

        country_completion_times =  eu_map.run_diffusion()

        print(f"Case Number {case_number}")
        for country in country_completion_times:
            print(f"{country.color}{country.name} {country.days_to_complete}{END_COLOR}")
        eu_map.display()
        print()
        case_number += 1


if __name__ == "__main__":
    simulate_euro_coins()