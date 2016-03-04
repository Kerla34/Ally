# import libraries
import numpy as np, matplotlib.pyplot as plt, matplotlib, pandas as pd, os
from preprocessing import preprocessing

rq = preprocessing()

#  Visualize 1st lines of the dataset

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
# Returning users within a certain time frame
# Define time frame, in our case let's say we want a weekly usage:
ret_tf = pd.Timedelta('7 days')
# Calculate column query_time - previous(query_time)
# Calculate first visit date
print(rq.iloc[0, 0])
c = len(rq.columns)
for n in range(len(rq.index)):
    uid = rq.iloc[n, 0]
    rq_temp = rq[rq['user_id'] == uid]
