#!/usr/bin/env python
import schedule
import winshell
import time
import os
import shutil

winTempFiles = r'C:\Users\bryan\AppData\Local\Temp'
winTemp2Files = r'C:\Windows\Temp'
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

schedule.every(1).hour.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)