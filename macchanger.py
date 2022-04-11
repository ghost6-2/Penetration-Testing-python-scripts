import random
import os
from sre_constants import CALL
import subprocess
from webbrowser import get

def get_rand():
    return random.choice("abcdef0123456789")


def new_mac():
    new_mac = ""

    for i in range(0,5):
            new_mac += get_rand() + get_rand() + ":"
    new_mac +=get_rand()+get_rand()
    return new_mac

#print old mac address
print("Old mac address", (os.system("ifconfig eth0 | grep ether | grep -oE [0-9ABCDEF:]{17}")))
subprocess.call(["sudo","ifconfig","eth0","down"])
new_m = new_mac()
# setting new random MAC address
subprocess.call(["sudo","ifconfig","eth0","hw","ether","%s"%new_m]) 
subprocess.call(["sudo","ifocnfig","eth0","up"])
#print new mac address
print(os.os.system("ifocnfig eth0 | grep ether | grep -oE [0-9ABCDEF:]{17}"))
