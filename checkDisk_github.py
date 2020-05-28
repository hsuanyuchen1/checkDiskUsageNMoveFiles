import psutil
import shutil
import os


filePending = r"\\192.168.253.193\d$\\files\pending"
ctaPending = r"d:\files\pending"

diskUsage = psutil.disk_usage("d:/")
#if the available space is less than 50 GB
if diskUsage.free/1024/1024/1024 < 50:
    tdir = os.listdir(ctaPending)
    for ind in range(0,1000):
        try:
            shutil.move(os.path.join(ctaPending,tdir[ind]), os.path.join(filePending, tdir[ind]))
            print(tdir[ind])
        except:
            pass
else:
    print(diskUsage.free/1024/1024/1024)
