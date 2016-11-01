'''
    Here is where we run tests
    on the data collectors.
'''

from yelpDataCollector import *

yelpCollector = YelpDataCollector()


#print(yelpCollector.collect().businesses)

# print the names of each business
yelpCollector.collectAndStore()
