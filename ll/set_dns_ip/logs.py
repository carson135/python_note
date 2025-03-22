#!/usr/bin/env python
# coding=utf-8

import time
import os

def logs(log):
    fobj=open('./log','a+',encoding='utf-8')  #changed
    fobj.write(time.ctime())
    fobj.write(str(log)+'\n'+'pid:'+str(os.getpid())+'\n')
    fobj.close()

