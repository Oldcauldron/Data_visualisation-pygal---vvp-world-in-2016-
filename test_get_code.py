
import unittest
from get_code import bicode
from pygal.maps.world import COUNTRIES
import json


class GetCodeTestCase(unittest.TestCase):

    def test_all(self):
        self.assertEqual(bicode('Russian Federation'), 'ru')

    def test_libya(self):
        nic = ' not in COUNTRIES in '
        with open('gdp_json.json') as gdp:
            all_countr_1 = json.load(gdp)
        for countr in all_countr_1:
            if\
                    countr['Year'] == 1990 or\
                    countr['Year'] == 2016:
                try:
                    self.assertIn(countr['Country Name'], COUNTRIES)
                except AssertionError:
                        print(countr['Country Name'], nic, countr['Year'])


unittest.main()
