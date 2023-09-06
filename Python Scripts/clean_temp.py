#!/usr/bin/env python
import schedule
import winshell
import time
import os
import shutil

def job():
    for filename in os.listdir(winTempFiles):
        file_path = os.path.join(winTempFiles, filename)
        try:
         if os.path.isfile(file_path) or os.path.islink(file_path):
             os.unlink(file_path)
         elif os.path.isdir(file_path):
             shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    for filename in os.listdir(winTemp2Files):
        file_path = os.path.join(winTemp2Files, filename)
        try:
         if os.path.isfile(file_path) or os.path.islink(file_path):
             os.unlink(file_path)
         elif os.path.isdir(file_path):
             shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

schedule.every(10).seconds.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)