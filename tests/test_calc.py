# -*- coding: utf-8 -*-
# online Lunar Calendar: https://wannianrili.51240.com/
import datetime
from lunarcalendar._calc import specified_solar_term, annual_solar_terms


def test_calc():
    for year in range(1990, 2101):
        annual_solar_terms(year)
        for i in range(0, 24):
            if i < 22:
                assert specified_solar_term(year, i).year == year
            else:
                # minor cold(小寒) | major cold(大寒)
                assert specified_solar_term(year, i).year == year + 1
