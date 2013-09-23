#!/usr/bin/python
import os
import sys
import argparse

blocksize=256

files=os.listdir("output")

for f in files:
    fo=open("output/"+f, "r")
    fo.seek(0)
    counter=0
    while 1:
        byte=fo.read(1)
        if not byte:
            break
        index=counter%blocksize
        refile="replace/"+("%d" %index)+".rec"
        refo=open(refile, "a+")
        refo.write(byte)
        counter+=1