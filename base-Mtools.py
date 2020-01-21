#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: M00yy
# Time: 2020-01-21 
# Site: https://m00yy.github.io

'''
 __  __ _              _       _             __  __  ___   ___              
|  \/  | |_ ___   ___ | |___  | |__  _   _  |  \/  |/ _ \ / _ \ _   _ _   _ 
| |\/| | __/ _ \ / _ \| / __| | '_ \| | | | | |\/| | | | | | | | | | | | | |
| |  | | || (_) | (_) | \__ \ | |_) | |_| | | |  | | |_| | |_| | |_| | |_| |
|_|  |_|\__\___/ \___/|_|___/ |_.__/ \__, | |_|  |_|\___/ \___/ \__, |\__, |
                                     |___/                      |___/ |___/ 

by M00yy
'''
# V1.0.0

from optparse import *
import base64
import sys
import base64
import base36
import base58
import base62
import base91
import py3base92 as base92
import os
import string
# usage="python3 Mtools.py [options]"
banner = '''\033[32m
 __  __ _              _       _             __  __  ___   ___              \033[32m
|  \/  | |_ ___   ___ | |___  | |__  _   _  |  \/  |/ _ \ / _ \ _   _ _   _ \033[32m
| |\/| | __/ _ \ / _ \| / __| | '_ \| | | | | |\/| | | | | | | | | | | | | |\033[32m
| |  | | || (_) | (_) | \__ \ | |_) | |_| | | |  | | |_| | |_| | |_| | |_| |\033[32m
|_|  |_|\__\___/ \___/|_|___/ |_.__/ \__, | |_|  |_|\___/ \___/ \__, |\__, |\033[32m
                                     |___/                      |___/ |___/ \033[32m
                                                                            \033[33m https://m00yy.github.io\033[0m
'''

'''
python3 base-Mtools.py -c -t caesar
python3 base-Mtools.py -c|-d -m b64 -t 123 
'''

# parser=optparse.OptionParser(usage)
def move(ch: str, k: int):
    if ch.islower():
        i = string.ascii_lowercase.find(ch)
        return string.ascii_lowercase[(i + k) % 26]
    elif ch.isupper():
        i = string.ascii_uppercase.find(ch)
        return string.ascii_uppercase[(i + k) % 26]
    else:
        return ch
def caesar(text:str,k:int):
    cipher=''
    for i in text:
        cipher += move(i,k)
    return cipher

def main():
    usage = "[*] Usage: %prog <-e|-d> <-c|--Caesar> <-m|--method Method> -t TEXT "
    parser = OptionParser(version="1.0.0",usage=usage)
    # base16
    parser.add_option("-m","--method",dest="method",action="store",metavar="METHOD",help="which method")
    parser.add_option("-e","--encrypt",dest="deal",action="store_true",default="True",help="encrypt")
    parser.add_option("-d","--decrypt",dest="deal",action="store_false",help="decrypt")
    parser.add_option("-t","--text",dest="text",type="string",metavar="Text",help="input text")
    parser.add_option("-c","--Caesar",dest="caesar",action="store_true",help="Caesar Cipher")

    (options,args) = parser.parse_args()
    if options.caesar == True:
        print("[*] Finish!!")
        print()
        for cnt in range(26):
            print("[*] " + caesar(options.text,cnt))
        sys.exit()
    # encrypt
    if options.deal == True:
        if options.method in ["b16","base16"]:
            print("[*] Finish!!")
            print()
            print("[*] " + base64.b16encode(options.text.encode('utf-8')))
            sys.exit()
        elif options.method in ["b32","base32"]:
            print("[*] Finish!!")
            print()
            print("[*] " + base64.b32encode(options.text.encode("utf-8")))
            sys.exit()
        elif options.method in ["b64","base64"]:
            print("[*] Finish!!")
            print()
            print("[*] " + base64.b64encode(options.text.encode("utf-8")))
            sys.exit() 
        elif options.method in ["b85a","base85a"]:
            print("[*] Finish!!")
            print()
            print("[*] " + base64.a85encode(options.text.encode("utf-8")))
            sys.exit()
        elif options.method in ["b85b","base85b"]:
            print("[*] Finish!!")
            print()
            print("[*] " + base64.b85encode(options.text.encode("utf-8")))
            sys.exit()
        elif options.method in ["b91","base91"]:
            print("[*] Finish!!")
            print()
            print("[*] " + base91.encode(options.text.encode("utf-8")))
            sys.exit()
        elif options.method in ["b92","base92"]:
            print("[*] Finish!!")
            print()
            print("[*] " + base92.encode(options.text.encode("utf-8")))
            sys.exit()
        elif options.method in ["b36","base36"]:
            print("[*] Finish!!")
            print()
            print("[*] " + base36.loads(options.text))
            sys.exit()
        elif options.method in ["b58","base58"]:
            print("[*] Finish!!")
            print()
            print("[*] " + base58.b58encode(options.text))
            sys.exit()
        elif options.method in ["b62","base62"]:
            print("[*] Finish!!")
            print()
            print("[*] " + base62.encode(int(options.text)))
            sys.exit()
    else:
        if options.method in ["b16","base16"]:
            print("[*] Finish!!")
            print()
            print("[*] " + base64.b16decode(options.text.encode("utf-8")))
            sys.exit()
        elif options.method in ["b32","base32"]:
            print("[*] Finish!!")
            print()
            print()
            print("[*] " + base64.b32decode(options.text.encode("utf-8")))
            sys.exit()
        elif options.method in ["b64","base64"]:
            print("[*] Finish!!")
            print()
            print("[*] " + base64.b64decode(options.text.encode("utf-8")))
            sys.exit()
        elif options.method in ["b85a","base85a"]:
            print("[*] Finish!!")
            print()
            print("[*] " + base64.a85decode(options.text.encode("utf-8")))
            sys.exit()
        elif options.method in ["b85b","base85b"]:
            print("[*] Finish!!")
            print()
            print("[*] " + base64.b85decode(options.text.encode("utf-8")))
            sys.exit()
        elif options.method in ["b91","base91"]:
            print("[*] Finish!!")
            print()
            print("[*] " + base91.decode(options.text))
            sys.exit()
        elif options.method in ["b92","base92"]:
            print("[*] Finish!!")
            print()
            print("[*] " + base92.decode(options.text.encode("utf-8")))
            sys.exit()
        elif options.method in ["b36","base36"]:
            print("[*] Finish!!")
            print()
            print("[*] " + base36.dumps(int(options.text)))
            sys.exit()
        elif options.method in ["b58","base58"]:
            print("[*] Finish!!")
            print()
            print("[*] " + base58.b58decode(options.text))
            sys.exit()
        elif options.method in ["b62","base62"]:
            print("[*] Finish!!")
            print()
            print("[*] " + base62.decode(options.text))
            sys.exit()

if __name__ == '__main__':
    print(banner)
    main()