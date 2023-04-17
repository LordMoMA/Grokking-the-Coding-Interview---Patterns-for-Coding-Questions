import os
import time

while True:
    os.system('git add .')
    os.system('git commit -m "dfs"')
    os.system('git push -u origin main')
    time.sleep(900) # sleep for 5 min
