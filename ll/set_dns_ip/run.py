#!/usr/bin/python3.7
#

import time
import os
#import logs

def task():
    #print(os.getcwd())
    os.system('python3 /home/nova/python_note/ll/set_dns_ip/checkdnsip.py > /home/nova/python_note/ll/set_dns_ip/log.txt 2>&1 &')   #ipv4py
    #logs.logs('running...')

while True:
    task()
    time.sleep(1800)
