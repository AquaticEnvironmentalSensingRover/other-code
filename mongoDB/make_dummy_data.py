# Create some dummy data

import datetime
import time
import random
import pymongo
from pymongo import MongoClient

#{
#  ver : <float>
#  atype: <String>,
#  itype: <Integer> ,
#  vertype : <float> ,
#  ts : <timestamp> , # using simple time.time() initially but should change
#  param : <format depends on atype>
#  comment : <String> ,
#  message : <String>
#}
#
#ver - the global version of the data storage type
#atype - Typically 4 letter code
#itype - (optional) index that may also be used to identify the subunit e.g. Thermometer #1, #2 etc
#vertype - version of the data type
#comment -  (optional) comment about the data type
#ts - time stamp for the event
#param - format dependent on the atype
#message - (optional) addition information
#tags - (optional) an use to classify types of data


# Set up database connection
client = MongoClient()
db = client.test_database_param
collection = db.test_events2


for i in range(10) :
    # print i
    
    # Example of temperature entry
    newentry = { 
        'ver' : 1.0
        , 'atype' : 'TEMP'
        , 'itype' : i
        , 'vertpe' : 1.0
        , 'ts' : time.time()  # thsi time format may change 
        , 'param' : random.random()*30
        , 'paramunit' : 'degC'
        , 'comment' : 'Testing'
        , 'tags' : [ 'sampledata' ,  ]
        }    
    post_id = collection.insert_one( newentry )
 
    # Example of gps entry
    newentry = { 
        'ver' : 1.0
        , 'atype' : 'GPS'
        , 'itype' : 1
        , 'vertpe' : 1.0
        , 'ts' : time.time()  # thsi time format may change 
        , 'param' :  { 
        'x' : 1000. * random.random() 
        , 'y' : 1000. * random.random() 
        , 'xerror' : random.random() 
        , 'yerror' : random.random() 
        , 'z' : 100. * random.random()
        , 'zerrror' : 10. * random.random() 
        } 
        , 'paramunit' : 'degC'
        , 'comment' : 'Testing'
        }    
    post_id = collection.insert_one( newentry )
 
       
print "Total %d entries in the database" % collection.count()


