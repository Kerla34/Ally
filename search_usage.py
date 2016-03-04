# import libraries
import numpy as np, matplotlib.pyplot as plt, matplotlib, pandas as pd, os
from preprocessing import preprocessing

rq = preprocessing()

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
# rq_in_advance_filter['query_to_search_time'] = rq_in_advance_filter['query_to_search_time'].apply(
#    lambda x: x.total_seconds() ) # not working !!!
usage_in_advance = rq_in_advance_filter[rq_in_advance_filter['query_to_search_time'].value_counts()]
usage_in_advance.plot(kind='hist', alpha=0.5)
plt.show()



