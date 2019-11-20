# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 21:33:19 2019

@author: hsf
"""
import file_info

def get_record(filename):
    proj_list={}
    fmal=0
    fall=0
    with open(filename, 'r') as f:
        for line in f.readlines():
            result_mal=0
            result_all=0
            tokens=line.split()
            name=tokens[0][:-4]
            md5=tokens[1][4:]
            for token in tokens:
                if len(token)>9 and token[:8]=="results:":
                    
                    str_result=token[8:]
                    split_result=str_result.split('/')
                    result_mal=int(split_result[0])
                    result_all=int(split_result[1])
                    break
            if result_all!=0:
                proj_list[name]=file_info.v_record(md5,name,result_mal,result_all)
                fall+=1
                if result_mal>=30:
                    fmal+=1
        print (fall,fmal)
        f.close()
    return proj_list
    