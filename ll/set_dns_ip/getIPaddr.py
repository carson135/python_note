#!/usr/bin/env python
#coding=utf-8

import requests
import socket
import os
import logs

#前面两个通过dns服务器获得本地IP地址，有时候获得的地址不准

def getAddr6():
    try:
        response=requests.request('get','https://ipv6.ddnspod.com')
        ip6='['+response.text+']'
        logs.logs(ip6)
        return response.text
    except:
        pass


def getAddr4():
    try:
        response=requests.request('get','https://ipv4.ddnspod.com')
        ip4=response.text
        logs.logs(ip4)
        return response.text
    except:
        pass

#获取域名当前的解析值
def getDomainIp(domain):
    try:
        ipad=socket.getaddrinfo(domain, None)
        logs.logs(ipad[0][4][0])
        return str(ipad[0][4][0])
    except:
        pass



#用于获取linux系统的全球ipv6地址，直接解析本地网络信息

def getIPv6ForLinux():
    ipaddr=''
    lines=os.popen('ifconfig').readlines()
    for i in lines:
        if ':' in i and 'inet6' in i and 'global' in i and '64' in i:
            tmp=i[-32:]
            if '64' in tmp:
                ipaddr=i.split(' ')

    for j in ipaddr:
        if ':' in j:
            result=j
            logs.logs(j)
    if ipaddr=='':
        logs.logs('ERROR!!!\n')
        exit('0')
    else:
        return result

