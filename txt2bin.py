#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
File:txt2bin.py
Author:todonyan
Description:テキストファイルとバイナリファイルの相互変換
-----------------------------------------------
〔変更履歴〕
2020/07/24 todonyan 新規作成
"""
import sys # for open()
import binascii # for binascii()

def main():
  infile=open(sys.argv[1] , "r")
  outfile=open(sys.argv[2] , "wb")
  while 1:
    msg = infile.read(2)# 2文字ずつ読込
    if not msg:break
    getBin = binascii.a2b_hex(msg)# 16進数文字列(bytes型)→バイナリ(bytes型)変換
    print(getBin)
    outfile.write(getBin)
  infile.close()
  outfile.close()

# エントリポイント
if __name__ == "__main__":
  main()
