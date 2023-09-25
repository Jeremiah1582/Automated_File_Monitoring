# here we have coded a watch-script that monitors the directory for CRUD changes. 
# every log is documented in log file 

# reference Source: https://www.youtube.com/watch?v=M9CT6MMry0U&ab_channel=JCharisTech 

import sys
import time
from watchdog.observers import Observer 
from watchdog.events import LoggingEventHandler
import logging
import getpass
import socket

SLEEPER=2
LOG_FILE_EXT ='.log'

#this class stops the script from acknowledging changes to the dev.log file to prevent infinite loop
class CustomLoggingEventHandler(LoggingEventHandler):
    def on_modified(self, event):
        if not event.src_path.endswith(LOG_FILE_EXT):
            return super().on_modified(event)
        
    # backup the directory 
    # create a function for backing up files
    


# Observer - for monitoring directory or file for events 
if __name__ == '__main__': # this is a special line that’s used to make Python files usable as either reusable modules or standalone scripts. only executable directly
    # how to store the logs to a log file...
    # how to store who is making changes to the file...
    user = getpass.getuser()
    user_ip = socket.gethostbyname(socket.gethostname())
    logging.basicConfig(filename='dev.log', filemode='a', level=logging.INFO, #specifying the level of our logged info (log everything)
                        format ='%(asctime)s-%(process)d -%(message)s | ' + #how to format our logged data
                        f'  userId:{user} | IP:{user_ip} | ', #log the user that makes changes
                        datefmt='%Y-%m-%d %H:%M:%S | ' #logging the time event fired
                        )
    
    
    
    
    # directory or file i want to monitor 
    path = sys.argv[1] if len(sys.argv)>1 else '.' #path of the directory
    print(path)
    
    event_handler=CustomLoggingEventHandler()
    observer= Observer()
    observer.schedule(event_handler, path , recursive=True)
    observer.start()


    # 
    try:
        while True: 
            time.sleep(SLEEPER) #check the directory every 2 secs
    except KeyboardInterrupt: #monitoring when keyboard-event is detected
        observer.stop()
        observer.join()