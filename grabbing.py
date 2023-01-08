# Config
intervalSeconds = 0.5
durationSeconds = 5
cmd = "bash grabbing.sh"
logFile = "grabbing.log"
resetLog = True

# Main
import os
import time
import threading
from datetime import datetime

def work(num):
    timeStart = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    output = os.popen(cmd).read()
    time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    log = "\r\nLog by process {} ({} - {}): \r\n".format(num, timeStart, time) + output.strip() + "\r\n"
    f = open(logFile, "a")
    f.write(log)
    f.close()

# Main process
if __name__ == '__main__':
    processNum = int(round(durationSeconds / intervalSeconds))

    if resetLog:
        f = open(logFile, "w")
        # f.write(str(output))
        f.close()

    # print(processNum)
    threads = {}
    for i in range(processNum):
        threads[i] = threading.Thread(target=work, args = (i,))
        threads[i].start()
        time.sleep(intervalSeconds)

    # Wait for all workers to complete
    for i in threads:
        threads[i].join()

    print("\r\nDone. logFile: {}".format(logFile))
