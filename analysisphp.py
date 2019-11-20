# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:40:52 2019

@author: hsf
"""
import re

def analysisphp(filename):
    filetokendic={}
    print ("*************************")
    print (filename)

    with open(filename, 'r',errors='ignore') as f:
        for line in f.readlines():
            tokens=re.split(r"[!@#$%^&*()\-+=\[\]\|:;,.\"\'<>?/{} \n\\]",line)
            while '' in tokens:                   
                tokens.remove('')
            for token in tokens:

                if (token not in filetokendic and not token.isdigit() and
                    (token[0]<='z' and token[0]>='a' or token[0]<='Z' and
                     token[0]>='A' or token[0]=='_' or token[0]<='9' and token[0]>='0')):
                    filetokendic[token]=1
        f.close()
#        print (filetokendic)

    return filetokendic