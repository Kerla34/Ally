# import libraries
import numpy as np, matplotlib.pyplot as plt, matplotlib, pandas as pd, os

# The script was encapsulated as a function

def preprocessing():
    # Import the data file as a Pandas DataFrame
    path = os.getcwd()
    rq = pd.read_csv(path + '/data/route_queries.csv')

    # Check the columns and their data types

    # print(rq.dtypes) # Commented once preprocessing is encapsulated
    # Convert dates from object to date type:

    rq['query_time'] = (rq['query_time'].apply(pd.to_datetime))
    rq['search_time'] = (rq['search_time'].apply(pd.to_datetime))
    return rq
