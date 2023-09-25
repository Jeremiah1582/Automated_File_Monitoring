# Observer - for monitoring directory or file for events 

# Handler - manage the action to take on the event  

import sys
import time

if __name__ == '__main__':
    # directory or file i want to monitor 
    path = sys.argv[1] if len(sys.argv)>1 else '-'
    print(path)