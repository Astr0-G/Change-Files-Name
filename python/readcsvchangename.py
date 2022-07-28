import pandas as pd
import numpy as np
import os
from os import walk


def modify(path):
    csv_data = pd.read_csv('namesmodity.csv')
    before = csv_data["before"]
    data_before = list(np.array(before))
    after = csv_data["after"]
    data_after = list(np.array(after))
    count = 0
    filenames = next(walk(path), (None, None, []))[2]  # [] if no file
    for i in filenames:
        try:
            if i in data_before:
                numInList = data_before.index(i)
                oldName = path + i
                newName = path + data_after[numInList]
                os.rename(oldName, newName)
                print('{} has changed to {}.'.format(i, data_after[numInList]))
                count += 1
        except:
            pass
    if count == 0:
        print('Folders directory path wrong or there is no files in the directory, Please try again...')
    if count > 0:
        print('Work Done! Modified {} files.'.format(count))


if __name__ == "__main__":
    print(r'Please enter directory path(example: D:\Project\folders\)：')
    directoryPath = input()
    filescheck = next(walk(directoryPath), (None, None, []))[2]
    if filescheck:
        modify(directoryPath)
    else:
        print('Folders directory path wrong or there is no files in the directory, Please try again...')
