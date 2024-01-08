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
    periods = string.split(';')[:-1]

    num_rows = 0
    num_cols = len(periods) + 1

    period_nums = []
    prices = {}
    for index, period in enumerate(periods):        # Iterate thru the periods
        
        elements = period.split(':L')               # Split rates/prices from periods
        period_nums.append(elements[-1])            # append period to list
        price_rate = elements[0].split(',')         # Split the rates and prices

        # This is the first period
        if index == 0:

            num_rows = len(price_rate) // 2 + 1     # Get the number of rows (rate, price, rate, ...)
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

    # Iterate thru the price dictionary for rates and prices
    for index, (key, value) in enumerate(prices.items(), start=1):
        matrix[index][0] = key                      # Add the rate to the first column
        matrix[index, 1:] = value                   # Add the rates prices to the matrix

    return matrix                                   # Return string matrix

# ==============================================================================================
def method_2(string: str):

    # Split price periods
    # Gives: ["5.50,1000,5.00,1020,6.00,1030:L100", "5.50,1010,5.00,1050,6.00,990:L200"]
    periods = string.split(';')[:-1]

    # Split rates and prices from period numbers
    # Gives: [("5.50,1000,5.00,1020,6.00,1030", "100"), ("5.50,1010,5.00,1050,6.00,990", "200")]
    rates_periods = [tuple(period.split(':L')) for period in periods]
    
    # Slit the rates and prices
    # Gives: [(["5.50", "1000", "5.00", "1020", "6.00", "1030"], "100"), ...]
    data = [(rate.split(','), period) for rate, period in rates_periods]

    # Separate data into rates, prices, and periods
    # Gives: ['5.50', '5.00', '6.00']
    rates = {}
    periods = []
    for r,p in data:

        # Iterate thru the prices and rates
        for i in range(0, len(r), 2):

            # add the price to the rate
            if r[i] in rates:
                rates[r[i]].append(r[i+1])
            # Init rate with first price
            else:
                rates[r[i]] = [r[i+1]]            

        # Add to list of periods
        periods.append(p)
    
    num_rows = len(rates) + 1
    num_cols = len(rates_periods) + 1

    # Initializing matrix
    matrix = np.full((num_rows, num_cols), '', dtype='<U10')
    # Adding periods to matrix
    matrix[0, 1:] = periods

    # Adding prices and rates to matrix
    for i, (rate,price)  in enumerate(rates.items(), start=1): 
        matrix[i][0] = rate
        matrix[i, 1:] = price      
    
    return matrix

# ==============================================================================================
def method_3(string:str):
    # Current string being tracted
    rate = ''
    price = ''
    periods = []
    rates = {}

    delim = [',', ':', ';', 'L']

    track = False

    for c in string:        

        # A price has been completed
        if (c == ',' or c ==':') and track:

            # Add the price to the rate
            if rate in rates:
                rates[rate].append(price)
            # Init rate in dictionary
            else:
                rates[rate] = [price]

            # Reset the rate and price variables
            rate, price = '', ''
            track = False

        # A rate has been completed
        elif c == ',' and not track:
            track = True

        # A period has been completed
        elif c == ';' and not track:
            periods.append(rate)
            rate = ''

        # Process rate
        elif not track and c not in delim:
            rate += c
        # Process price
        elif track and c not in delim:
            price += c

    n_row = len(rates) + 1
    n_col = len(periods) + 1

    # Init matrix with empty strings
    matrix = np.full((n_row,n_col), '', dtype='<U10')
    # Add periods to first row
    matrix[0, 1:] = periods

    # Add rates and prices to matrix
    for i,(key,value) in enumerate(rates.items(), start=1):
        matrix[i][0] = key
        matrix[i, 1:] = value

    return matrix

# ==============================================================================================
if __name__ == "__main__":
    string = "5.50,1000,5.00,1020,6.00,1030:L100;5.50,1010,5.00,1050,6.00,990:L200;"

    #print(method_1(string))
    print(method_2(string))
    print(method_3(string))