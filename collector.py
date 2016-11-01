'''
    The data accumulator is the most basic
    unit of data collection.

    It can both take data from a website,
    and place it in a database.


    All data can be collected as a tree
    of search terms.


    You should be able to answer the question:
        I want this data from this source,
        and I want to do this with it.


    DataCollector ==> Database ==> Graphs ==> Presentation
        \
         \
         Graphs

    What do I want?
        Do I want historic data?
            If so, start saving that data to the the database.


    Interface:
        commands:

    Show sources:
        Yelp
        Craigslist
        Meetup
        ... etc.






'''

class DataCollector:

    def collect(self):
        pass
    def store(self):
        pass
