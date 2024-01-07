'''
Convert a string to a matrix with the following pattern:
    5.5,100,5.0,102,6.0,103:L10;5.5,101,5.0,105,6.0,99:L20;.....

The resulting matix should look like the following:

            lock_1      lock_2      ...     lock_m
    rate_1  price_1_1   price_1_2           price_1_m

    rate_2  price_2_1

    ...

    rate_n  price_n_1   ...                 price_n_m


The example string will give:

            10      20
    5.5     100     101

    5.0     102     105

    6.0     103     99
'''
import numpy as np

def method_1(string:str):

    # Split the string into individual periods
    # Gives: ["5.5,100,5.0,102,6.0,103:L10", ...]
    periods = string.split(';')
    periods.pop()

    num_rows = 0
    num_cols = len(periods) + 1

    period_nums = []
    prices = dict()
    for index, period in enumerate(periods):        # Iterate thru the periods
        
        elements = period.split(':L')               # Split rates/prices from periods
        period_nums.append(elements[-1])            # append period to list
        price_rate = elements[0].split(',')         # Split the rates and prices

        # This is the first period
        if index == 0:

            num_rows = int(len(price_rate) / 2) + 1 # Get the number of rows (rate, price, rate, ...)
            for k in range(0, len(price_rate), 2):  # Iterate thru first prices to init dictionary

                prices[price_rate[k]] = [price_rate[k+1]]

        # Remaining periods
        else:
            for k in range(0, len(price_rate), 2):  # Iterate thru the remaining prices

                prices[price_rate[k]].append(price_rate[k+1])
    
    # Init matrix: rate x period
    matrix = np.full((num_rows, num_cols), '', dtype='<U10')

    for i, p in enumerate(period_nums):             # Add the period labels to the top of the matrix
        matrix[0][i+1] = p

    index = 1
    for key, value in prices.items():               # Iterate thru the price dictionary
        matrix[index][0] = key                      # Add the rate to the first column

        for i, p in enumerate(value):               # Add the prices of the rate to the row
            matrix[index][i+1] = p

        index += 1

    return matrix                                   # Return string matrix

# ==============================================================================================
def method_2(string: str):
    periods = string.split(';')[:-1]
    num_cols = len(periods) + 1

    period_nums = [period.split(':L')[-1] for period in periods]

    prices = {}
    num_rows = 0

    for index, period in enumerate(periods):
        price_rate = period.split(':L')[0].split(',')
        
        if index == 0:
            num_rows = len(price_rate) // 2 + 1
            prices = {price_rate[k]: [price_rate[k + 1]] for k in range(0, len(price_rate), 2)}
        else:
            for k in range(0, len(price_rate), 2):
                prices.setdefault(price_rate[k], []).append(price_rate[k + 1])

    matrix = np.full((num_rows, num_cols), '', dtype='<U10')

    for i, p in enumerate(period_nums):
        matrix[0][i + 1] = p

    for index, (key, value) in enumerate(prices.items(), start=1):
        matrix[index][0] = key
        matrix[index, 1:] = value  # Assign the entire row at once

    return matrix

if __name__ == "__main__":
    string = "5.5,100,5.0,102,6.0,103:L10;5.5,101,5.0,105,6.0,99:L20;"

    print(method_2(string))