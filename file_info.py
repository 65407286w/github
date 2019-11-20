# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 18:03:35 2019

@author: hsf
"""

class file_info:
    def __init__(self, file_name,md5,result_mal,result_all):
        self.filename=file_name
        self.md5=md5
        self.result_mal=result_mal
        self.result_all=result_all
        self.filetokens={}
class v_record:
    def __init__(self, md5,name,result_mal,result_all):
        self.md5=md5
        self.result_mal=result_mal
        self.result_all=result_all
        self.name=name