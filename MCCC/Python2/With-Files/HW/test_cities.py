#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest

from city_functions import place #from file import the function

class CitiesTestCase(unittest.TestCase):
    
    def test_city_country(self):
        result = place("Ottawa", "Canada")
        self.assertEqual(result, "Ottawa, Canada")
        
    def test_city_country_population(self):
        result = place("Anchorage", "United States", 288000)
        self.assertEqual(result, "Anchorage, United States - population 288,000")

unittest.main()
        

