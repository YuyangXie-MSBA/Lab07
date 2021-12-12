#!/usr/bin/env python3

import sys

def reducer():
    salesMax = 0
    oldKey = None
    oldItem = None

    for line in sys.stdin:
        data = line.strip().split(",")
        
        thisKey, thisItem, thisCost = data
        if oldKey is not None and oldKey == thisKey and oldItem != thisItem:
            print (oldKey + "," + oldItem + "," + str(salesMax))
            salesMax = 0
        if oldKey is not None and oldKey != thisKey:
            print (oldKey + "," + oldItem + "," + str(salesMax))
            salesMax = 0

        if float(thisCost) > salesMax:
            salesMax = float(thisCost)
        
        oldKey = thisKey
        oldItem = thisItem
        
    if oldKey is not None: # for the final key
        print (oldKey + "," + oldItem + "," + str(salesMax))
        
if __name__ == "__main__":
    # what function should run when python reducer.py is called?
    reducer()
