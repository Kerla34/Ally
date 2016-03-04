__author__ = 'thomas'

# Alright ! Let's do this
# We have csv file containing data from Ally app
# The idea will be to extract as many insights as possible
# Let's first start by importing the file


# import libraries
import numpy as np, matplotlib.pyplot as plt, matplotlib, pandas as pd, os

# Import the data file as a Pandas DataFrame
path = os.getcwd()
rq = pd.read_csv(path + '/data/route_queries.csv')

# Check the columns and their data types

print(rq.dtypes)
# Convert dates from object to date type:

rq['query_time'] = (rq['query_time'].apply(pd.to_datetime))
rq['search_time'] = (rq['search_time'].apply(pd.to_datetime))

print(rq.dtypes)


# Visualize 1st lines of the dataset

print(rq.head(2))
print('\n')
# What is the size of our sample ?
rq_size = len(rq.index)
print('Number of events: ' + str(rq_size))
print(rq.columns)  # Column names
# How many unique users ? And how many time did they use the app

users = rq[rq.columns[0]].value_counts()
#print(users)
number_users = len(users.index)
print('Number of unique users: ' + str(number_users))
print(users)
# The first user appear almost 7000 times ! It's quite huge, let's remove it for visualisation reason.
# Showing the number of use from the 20 first customers except our guy.
#users2 = users[1:20]
#users2.plot(kind='bar')
#plt.show()
# Thomas : Is that really useful ??

# How many users have used the app more than once ?
print(str(len(users[users>1])) + ' users are recurring users over all time')
print('They represent ' + str(100*round(len(users[users>1]) / number_users,4)) + '% of the total number of users')
print('\n')

# Returning users within a certain time frame
# Define time frame
# Calculate column query_time - previous(query_time)
ret_tf = 'one month'

# Are users searching their route in advance or at last minute ?

rq['query_to_search_time'] = rq['search_time'] - rq['query_time']
print(rq['query_to_search_time'])
# Negative values are due to the small delay between app opening and the actual time the user
# tap the search button. We can see that they are really small.
# They should not be considered for our use case... BUT they give us
# a very useful information: the time to complete the form !
# It's actually an indicator we could use for UX evaluation (and improvement)

# Let's check how much time in advance the user look for a route
rq_in_advance = rq[rq['query_to_search_time'] > pd.Timedelta('0 days')]
print(rq_in_advance['query_to_search_time'].describe())

print(str(len(rq_in_advance.index)) + ' events are use to check the route in advance, they represent ' +
      str(round(len(rq_in_advance.index) / rq_size * 100, 2)) + '% of our the app usage')

# Looks like there are some outliers here, some people searching for long time in the future.. Doesn't look like
# a normal usage of Ally, let's limit it to 30 days in the future to exclude extreme cases.
rq_in_advance_filter = rq_in_advance[rq_in_advance['query_to_search_time'] < pd.Timedelta('30 days')]
print(rq_in_advance_filter['query_to_search_time'].describe())
rq_in_advance_filter2 = rq_in_advance[rq_in_advance['query_to_search_time'] > pd.Timedelta('30 days')]
print(rq_in_advance_filter2['query_to_search_time'].describe())
# Let's describe the distribution of this usage in a histogram, per hour
rq_in_advance_filter['query_to_search_time'] = rq_in_advance_filter['query_to_search_time'].apply(
    lambda x: x.total_seconds() ) # not working !!!
usage_in_advance = rq_in_advance_filter[rq_in_advance_filter['query_to_search_time'].value_counts()]
usage_in_advance.plot(kind='hist', alpha=0.5)
plt.show()
