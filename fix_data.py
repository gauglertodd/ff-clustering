''' This script trims useless data from the EC rankings, and
makes sure that some useful data is added to our pandas DF '''
import csv
import os
import pandas as pd
from pandas import DataFrame


def trim_rankings():
    ''' this function does stuff '''
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "Rankings")
    file_names = os.listdir(directory)
    with open(directory + "/"  + file_names[1], 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print ', '.join(row)
trim_rankings()
