''' This file offers a selection of clustering algorithms, and calls upon the
other scripts in order to generate tier diagrams of fantasy football players.'''

from clustering import *
from fix_data import *
from get_rankings import *

def main():
    '''docstring'''
    print "Getting rankings...."
    get_ranks(True)
    get_ranks(False)
    print "Done. Saving rankings..."
    save_rankings()
    print "Done"

main()
