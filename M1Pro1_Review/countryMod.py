# Asking a user for country code, measure, find value in dict and display result then repeat or stop. 
# 09/06/2025
# CSC-221 M1Pro – Review
# Haylee Paredes

''' **Key** (for reference)
    cData = country data.
    cMeasure = country measure

Step 1: add dict. data from textbook.
Step 2: define func. for coundtry data. 
Step 3: define func. for measure. 
'''

allData = {
    'US': {'pop': 325.7, 'gdp': 19.39, 'ccy': 'USD', 'fx': 1.0},
    'CA': {'pop': 36.5,  'gdp': 1.65,  'ccy': 'CAD', 'fx': 1.35},
    'MX': {'pop': 129.2, 'gdp': 1.15,  'ccy': 'MXN', 'fx': 19.68}
}

def cData(code):
    """
    Parameters:
        code: str (country code in uppercase)
        
    Returns: dict if found, else empty dict.
    """
    if code in allData:
        return allData[code]
    else: 
        return {}

def cMeasure(data, measure):
    """
    Parameters:
        data: dict (statistics for one country)
        measure: str (measure name in lowercase)
        
    Returns: value if found, else empty str.
    """
    if measure in data:
        return data[measure]
    else:
        return ""