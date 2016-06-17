# Example of reading from database and plotting results


import datetime
import time
import random
import pymongo
from pymongo import MongoClient
import numpy as np
import matplotlib.pyplot as plt 


# Set up database connection
client = MongoClient()
db = client.test_database_param
collection = db.test_events2

print "Total %d entries in the database" % collection.count()

# Example of data ranges - doesn't work yet
#dstart = datetime.datetime(2016, 06, 15, 12)
#dstop = datetime.datetime(2016, 06, 17, 12)
#for post in posts.find({"date": {"$lt": dstop}}).sort("author"):
#    print post


# Get TEMP records sorted in time order
for i , post in enumerate( collection.find({"atype": {"$eq": "TEMP"}}).sort("ts") ):
    print post

# Get TEMP records and load into numpy array
# Should really error trap in case the relevant info is not actually available

print "\n\nCreate 2D Numpy Array for plotting"
 # Create numpy arrays 
datatime = np.zeros( [0 , ] , dtype = float )
datatemp = np.zeros( [0 , ] , dtype = float )

# 2D Version
# x2 = np.zeros( [0 , 2] , dtype = float )
for i , post in enumerate( collection.find({"atype": {"$eq": "TEMP"}}).sort("ts") ) :
    if i==0 :
        t0 = post['ts'] # Start time for this data set
    # x2 = np.append( x2 , [   [ post['ts'] - t0 , post['param'] ]   ], axis=0) # This is a very slow/ineffcient way to expand numpy arrays but ok for now
    datatime = np.append( datatime , [ post['ts'] - t0  ], axis=0)
    datatemp = np.append( datatemp , [ post['param']  ], axis=0)

plt.figure(1)
plt.clf()
plt.plot( datatime , datatemp , 'r+-' )
plt.show( )

