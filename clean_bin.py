#!/usr/bin/env python
import schedule
import winshell
import time
import os
import shutil

winTempFiles = r'C:\Users\bryan\AppData\Local\Temp'
# Importing the required modules
def job():    
    try:
	    winshell.recycle_bin().empty(confirm=False,
		    show_progress=False, sound=True)

# Print that the deletion in successful
	    print("Recycle Bin is emptied now!")

    except:
	    # Printing that the Recyclce-Bin is already Empty!
	    print("Recycle Bin is already empty!")

    #clean temp folder
    for filename in os.listdir(winTempFiles):
        file_path = os.path.join(winTempFiles, filename)
        try:
         if os.path.isfile(file_path) or os.path.islink(file_path):
             os.unlink(file_path)
         elif os.path.isdir(file_path):
             shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


schedule.every(10).seconds.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)