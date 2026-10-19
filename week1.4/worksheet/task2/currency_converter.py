
"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name: Steve
"""

def currency_converter(amount, from_currency, to_currency):

    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }
    
    # your code here
    base_currency = conversion_rate.get(from_currency)
    # stop the code from using invalid currency and the last condition stops bs from happening
    if ( base_currency is None ) or ( conversion_rate.get(to_currency) is None ) or ( from_currency is to_currency ): 
        return None
    elif amount < 0:
        return 0.0
    conversion = base_currency.get(to_currency)
    return amount * conversion

# Submit only this file currency_converter.py with the completed function.

# Remove any additional code you may have added during development and testing.
