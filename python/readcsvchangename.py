import pandas as pd
import numpy as np
import os
from os import walk


def modify(path):
    # read csv file
    csv_data = pd.read_csv('namesmodity.csv')
    
    # read csv file first column "before"
    before = csv_data["before"]
    data_before = list(np.array(before))
    
    # read csv file first column "after"
    after = csv_data["after"]
    data_after = list(np.array(after))
    
    # count for determine the success
    count = 0
    
    #check all files in the folders
    filenames = next(walk(path), (None, None, []))[2]  # [] if no file
    
    for i in filenames:
        # using try, except, due to any error happen in os.rename, take it out to find errors.
        try:
            # check if files names match the data we stored in csv file
            if i in data_before:
                numInList = data_before.index(i)
                oldName = path + i
                newName = path + data_after[numInList]
                
                #change the oldname to newname.
                os.rename(oldName, newName)
                print('{} has changed to {}.'.format(i, data_after[numInList]))
                
                #success count + 1
                count += 1
        except:
            pass
        
    # if there is no success, ask the user to check fold path.
    if count == 0:
        print('Folders directory path wrong or there is no files in the directory, Please try again...')
        
    # if there is success, give a final results.
    if count > 0:
        print('Work Done! Modified {} files.'.format(count))


if __name__ == "__main__":
    print(r'Please enter directory path(example: D:\Project\folders\ for windows; /Users/admin/projects/folders/ for macos)：')
    directoryPath = input()
    filescheck = next(walk(directoryPath), (None, None, []))[2]
    
    if filescheck:
        modify(directoryPath)
        
    # if filescheck returns [] which means there is no files in the folder or wrong folder name, do not move to the next function.
    else:
        print('Folders directory path wrong or there is no files in the directory, Please try again...')
