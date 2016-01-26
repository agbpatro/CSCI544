#!/usr/bin/python
import os
import sys
def giveByte(byte):
    byte = ord(byte)
    byte = bin(byte)[2:].rjust(8, '0')
    return byte
def convert(str):
    b_0 = "0000"
    b_7 = "0111"
    b_f = "1111"
    l1   = b_0+b_0+b_7+b_f
    l2   = b_0+b_7+b_f+b_f
    l3   = b_f+b_f+b_f+b_f
    if str <= l1:
        op =  "0" + str[9:16]
    elif str <= l2:
        op = "110"+str[5:10]+"10"+str[10:16]
    elif str <= l3:
        op = "1110"+str[0:4]+"10"+str[4:10]+"10"+str[10:16]
    return op
fn = sys.argv[1]
if os.path.exists(fn):
    fw = open("utf8encoder_out.txt", "wb")
    try:
        with open(fn, "rb") as fr:
            byte = fr.read(2)
            while byte:
                data_bin1 = giveByte(byte[0])+giveByte(byte[1])
                utf8 = convert(data_bin1)
                while len(utf8) > 1:
                    n = int(utf8[0:8], 2)
                    data = chr(n)
                    fw.write(data)
                    utf8 = utf8[8:]
                byte = fr.read(2)
    finally:
        fr.close()
        fw.close()
else:
    print "File does not exists"
