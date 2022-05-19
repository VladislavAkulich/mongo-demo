import psutil

from time import sleep


while True:
    print("The CPU usage is : ", psutil.cpu_percent(4))
    print(print('RAM memory % used:', psutil.virtual_memory()[2]))

    sleep(5)