#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# Author: M00yy
# Time: 2020-01-19 
# Site: https://m00yy.github.io

'''
base+Caesar的整合，快速的解题。by M00yy
'''

import base64
import base36
import base58
import base62
import base91
import py3base92 as base92
import sys
import os
import string


banner = '''\033[32m
 __  __ _              _       _             __  __  ___   ___              \033[32m
|  \/  | |_ ___   ___ | |___  | |__  _   _  |  \/  |/ _ \ / _ \ _   _ _   _ \033[32m
| |\/| | __/ _ \ / _ \| / __| | '_ \| | | | | |\/| | | | | | | | | | | | | |\033[32m
| |  | | || (_) | (_) | \__ \ | |_) | |_| | | |  | | |_| | |_| | |_| | |_| |\033[32m
|_|  |_|\__\___/ \___/|_|___/ |_.__/ \__, | |_|  |_|\___/ \___/ \__, |\__, |\033[32m
                                     |___/                      |___/ |___/ \033[32m
                                                                            \033[33m https://m00yy.github.io\033[0m
'''

Usage = 'Usage: python3 Mtools.py [options]'
options = '''
-h --help                        Show basic help message and exit
-b16 encrypt/decrypt  text       encrypt/decrypt base16
-b32 encrypt/decrypt  text       encrypt/decrypt base32
-b36 encrypt/decrypt  text       encrypt/decrypt base36
-b58 encrypt/decrypt  text       encrypt/decrypt base58
-b62 encrypt/decrypt  text       encrypt/decrypt base62
-b64 encrypt/decrypt  text       encrypt/decrypt base64
-b85a encrypt/decrypt text       encrypt/decrypt base85 module a
-b85b encrypt/decrypt text       encrypt/decrypt base85 module b
-b91 encrypt/decrypt  text       encrypt/decrypt base91
-b92 encrypt/decrypt  text       encrypt/decrypt base92
-Caesar -c            text       Caesar
'''

h = sys.argv[1]

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
    
if __name__ == '__main__':
    print(banner)
    print(Usage)
    print()

    if h == '-h' or h == '--help':
        print(options)
        exit(0)
    elif h == "-Caesar" or h == "-c":
        op = sys.argv[2]
        # if h == "-Caesar" or h == "-c"):
        for i in range(26):
            print(caesar(op,i))
        exit(0)
    else :
        op = sys.argv[2]
        text = sys.argv[3]
        # base64
        if h == "-b64" and (op == "encrypt" or op == "e"):
            text = text.encode("utf-8")
            print(base64.b64encode(text))
            exit(1)
        elif h == "-b64" and (op == "decrypt" or op == "d"):
            text = text.encode("utf-8")
            print(base64.b64decode(text))
            exit(2)
        # base16
        elif h == "-b16" and (op == "decrypt" or op == "d"):
            text = text.encode("utf-8")
            print(base64.b16decode(text))
            exit(3)
        elif h == "-b16" and (op == "encrypt" or op == "e"):
            text = text.encode("utf-8")
            print(base64.b16decode(text))
            exit(4)
        # base32
        elif h == "-b32" and (op == "decrypt" or op == "d"):
            text = text.encode("utf-8")
            print(base64.b32decode(text))
            exit(5)
        elif h == "-b32" and (op == "encrypt" or op == "e"):
            text = text.encode("utf-8")
            print(base64.b32encode(text))
            exit(6)
        # base85 a
        elif h == "-b85a" and (op == "decrypt" or op == "d"):
            text = text.encode("utf-8")
            print(base64.a85decode(text))
            exit(7)
        elif h == "-b85a" and (op == "encrypt" or op == "e"):
            text = text.encode("utf-8")
            print(base64.a85encode(text))
            exit(8)
        # base85 b
        elif h == "-b85b" and (op == "decrypt" or op == "d"):
            print(base64.b85decode(text))
            exit(9)
        elif h == "-b85b" and (op == "encrypt" or op == "e"):
            text = text.encode("utf-8")
            print(base64.b85encode(text))
            exit(10)
        # base62
        elif h == "-b62" and (op == "encrypt" or op == "e"):
            print(base62.encode(int(text)))
            exit(11)
        elif h == "-b62" and (op == "decrypt" or op == "d"):
            print(base62.decode(text))
            exit(12)
        # base91
        elif h == "-b91" and (op == "decrypt" or op == "d"):
            print(base91.decode(text))
            exit(13)
        elif h == "-b91" and (op == "encrypt" or op == "e"):
            text = text.encode("utf-8")
            print(base91.encode(text))
            exit(14)
        # base92
        elif h == "-b92" and (op == "decrypt" or op == "d"):
            print(base92.decode(text))
            exit(15)
        elif h == "-b92" and (op == "encrypt" or op == "e"):
            text = text.encode("utf-8")
            print(base92.encode(text))
            exit(16)   
        # base36
        elif h == "-b36" and (op == "decrypt" or op == "d"):
            print(base36.dumps(int(text)))
            exit(17)
        elif h == "-b36" and (op == "encrypt" or op == "e"):
            print(base36.loads(text))
            exit(18)     
        # base58
        elif h == "-b58" and (op == "decrypt" or op == "d"):
            print(base58.b58decode(text))
            exit(19)
        elif h == "-b58" and (op == "encrypt" or op == "e"):
            print(base58.b58encode(text))
            exit(20)