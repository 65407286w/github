#/usr/bin/python#coding=utf-8
import os,sys 
import zipfile
import shutil
import analysisphp
import file_info
import virsustotal_record
open_path='d:\\data'
save_path='d:\\data2' 
os.chdir(open_path)
tokens_map={}
token_num=0
proj_info={}
proj_num=0
tokens_w={}
tokens_b={}
#转到路径
#首先，通过zipfile模块打开指定位置zip文件
#传入文件名列表，及列表文件所在路径，及存储路径
def analysisfile(files_path,file_name):
    global token_num,proj_num
    proj_token={}
    
    k=0
    print ("-----------------------")
    for file_path,sub_dirs,files in os.walk(files_path):
        if k==1:
            del_path=file_path
        
        #print (file_path,files)   
        for file in files:
            if (len(file)>3 and file[-3:]==".js" or 
                len(file)>4 and file[-4:]==".php"):
                filetokensdic=analysisphp.analysisphp(file_path+"\\"+file)                
                for filetoken in filetokensdic:
                    if filetoken not in tokens_map:
                        token_num+=1
                        tokens_map[filetoken]=token_num
                    if filetoken not in proj_token:
                        proj_token[filetoken]=tokens_map[filetoken]
        k+=1
    
    print (proj_num)
    shutil.rmtree(del_path)
                        
        
        #print ("==================")
    if len(proj_token)!=0:
        proj_info[file_name]=file_info.file_info(file_name,v_record[file_name].md5,v_record[file_name].result_mal,v_record[file_name].result_all)
        for token in proj_token:
            proj_info[file_name].filetokens[token]=proj_token[token]
            if proj_info[file_name].result_mal>0:
                if token not in tokens_b:
                    tokens_b[token]=1
                else:
                    tokens_b[token]+=1
                if token not in tokens_w:
                    tokens_w[token]=0
            if proj_info[file_name].result_mal==0:
                if token not in tokens_w:
                    tokens_b[token]=1
                else:
                    tokens_b[token]+=1
                if token not in tokens_b:
                    tokens_w[token]=0
        proj_num+=1
    return

def Decompression(files,file_path,save_path):  
    os.getcwd()#当前路径  os.chdir(file_path)#转到路径  
    i=0
    for file_name in files:   

        if  file_name[:-4] in v_record:
            print ("yes")
            i+=1
            print(file_name)   
            r = zipfile.is_zipfile(file_name)#判断是否解压文件   
            if True:      
                zpfd = zipfile.ZipFile(file_name)#读取压缩文件     
                os.chdir(save_path)#转到存储路径      
                zpfd.extractall()      
                zpfd.close()

    
                #print (save_path+"\\"+file_name)
                analysisfile(save_path,file_name[:-4])
    
    
    
                print (i)
    #for p_info in proj_info:
    #    print (p_info.filename,p_info.filenum,p_info.filetokens)
def files_save(open_path): 
    for file_path,sub_dirs,files in os.walk(open_path):#获取所有文件名，路径   
  
        Decompression(files,file_path,save_path)
v_record=virsustotal_record.get_record("d:\\report_coinhive.txt")
'''
files_save(open_path)
for token in tokens_map:
    if token in tokens_b and token in tokens_w:
        if tokens_b[token]+tokens_w[token]>1:
            print (token,tokens_b[token],tokens_w[token])
        
    
'''    
    