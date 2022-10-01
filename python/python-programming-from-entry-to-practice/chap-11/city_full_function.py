# -*- coding: utf-8 -*-


def get_format_city(city, country, population):
    return city.lower().title() + ',' + country.lower().title(
    ) + ' - population ' + str(population)
