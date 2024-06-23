import subprocess
import sys

def install_package(package):
    """Install package using pip."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Attempt to import necessary libraries and install if they are missing
libraries = {
    'schedule': 'schedule',
    'winshell': 'winshell',
}

for lib, package in libraries.items():
    try:
        globals()[lib] = __import__(lib)
    except ImportError:
        print(f"{lib} not found. Installing...")
        install_package(package)
        globals()[lib] = __import__(lib)

import schedule
import winshell
import time
import os
import shutil
import traceback

# Define the directories
winTempFiles = os.getenv('TEMP')
winTemp2Files = os.getenv('TMP')
browser_cache_dirs = [
    os.path.expanduser('~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache'),
    os.path.expanduser('~\\AppData\\Local\\Mozilla\\Firefox\\Profiles')
]

def job():
    try:
        # Clean TEMP and TMP directories
        for temp_dir in [winTempFiles, winTemp2Files]:
            if os.path.exists(temp_dir):
                for filename in os.listdir(temp_dir):
                    file_path = os.path.join(temp_dir, filename)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                        print(f'Deleted {file_path}')
                    except (PermissionError, OSError) as e:
                        print(f'Failed to delete {file_path}. It may be in use by another process. Reason: {e}')
                    except Exception as e:
                        print(f'Failed to delete {file_path}. Reason: {e}')
            else:
                print(f"Path does not exist: {temp_dir}")

        # Clean the recycle bin
        try:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
            print('Recycle bin emptied')
        except Exception as e:
            print(f'Failed to empty recycle bin. Reason: {e}')

        # Clear browser caches
        for cache_dir in browser_cache_dirs:
            if os.path.exists(cache_dir):
                for filename in os.listdir(cache_dir):
                    file_path = os.path.join(cache_dir, filename)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                        print(f'Deleted {file_path}')
                    except (PermissionError, OSError) as e:
                        print(f'Failed to delete {file_path}. It may be in use by another process. Reason: {e}')
                    except Exception as e:
                        print(f'Failed to delete {file_path}. Reason: {e}')
            else:
                print(f"Path does not exist: {cache_dir}")

        # Run disk cleanup
        try:
            subprocess.run(['cleanmgr', '/sagerun:1'], check=True)
            print('Disk cleanup executed')
        except Exception as e:
            print(f'Failed to run disk cleanup. Reason: {e}')
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()
print("Your PC is being cleaned and optimized every 15 minutes, close the console anytime to stop the process.")
# Schedule the job every 15 minutes
schedule.every(15).minutes.do(job)

# Run the schedule
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Program terminated by user.")
except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()
finally:
    input("Press Enter to exit...")

