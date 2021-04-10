#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def place(city, country, pop=0):
    """Identifies a city within a country and it's population
    
    >>> place("Ottawa", "Canada", "934,243")
    'Ottawa, Canada - population 934,243'
    
    >>> place("Anchorage", "United States", 288000)
    'Anchorage, United States - population 288000'
    """
    
    if pop == "": 
        return f"{city}, {country}"
    else: 
        return f"{city}, {country} - population {pop:,}"

