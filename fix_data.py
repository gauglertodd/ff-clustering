''' This script trims useless data from the EC rankings, and
makes sure that some useful data is added to our pandas DF '''
import os
import numpy as np


def save_rankings():
    ''' this function "cleans" and stores EC rankings'''
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "Rankings")
    file_names = os.listdir(directory)
    # 0: Rank
    # 1: Player Name
    # 2: Position
    # 3: Team
    # 4: Bye Week
    # 5: Best Rank
    # 6: Worst Rank
    # 7: Avg Rank
    # 8: Std Dev
    # 9: ADP
    save_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  "Saved")

    for i in range(1, len(file_names)):
        filename = directory + "/" + file_names[i]
        save_file_name = save_directory + "/" + file_names[i][:-4] + ".npy"
        thedata = np.genfromtxt(
            filename,                      # file name
            skip_header=5,                 # lines to skip at the top
            skip_footer=0,                 # lines to skip at the bottom
            delimiter='\t',                # column delimiter
            dtype='string',                # data type
            filling_values=0,              # fill missing values with 0
            usecols=(1, 5, 6, 7, 8, 9),    # columns to read
            )
        np.save(save_file_name, thedata)
