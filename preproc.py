#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tika import parser
from konlpy.tag import Kkma
from hanspell import spell_checker
from PyPDF2 import PdfFileReader
from pdfrw import PdfReader
import re
import sys
import json
import os

def init(path):
    os.rename(path,'temp.pdf')
    
    txtpath=path[0:len(path)-4]+".txt"
    pathlist=path.split('/')
    pathlist[len(pathlist)-1]='temp.pdf'
    pdfpath='/'.join(pathlist)
    
    
    text=parser.from_file(pdfpath)
    text=delete_newline(text['content'])
    
    sentence=sentences(text)
    delete_index(sentence)
    spell_check(sentence)
    
    fp=open(txtpath,'w')
    print(sentence,file=fp)
    fp.close()
    os.remove(pdfpath)
    print(txtpath)

def spell_check(sentence):
    pattern=re.compile(' ')
    pattern2=re.compile('-\d*-')
    for idx in range(len(sentence)):
        sentence[idx]=re.sub(pattern,'',sentence[idx])
        sentence[idx]=re.sub(pattern2,'',sentence[idx])
        result=spell_checker.check(sentence[idx])
        sentence[idx]=result.checked.replace(u'\xa0','')
    
def delete_newline(text):
    pattern=re.compile('\n')
    text=re.sub(pattern,'',text)
    return text

def sentences(text):
    kkma=Kkma()
    sentence=kkma.sentences(text)
    del kkma
    return sentence

def delete_index(sentence):
    r=re.compile("목차|목 차")
    for idx in range(len(sentence)):
        if r.search(sentence[idx]) is not None:
            del sentence[idx]
            break 

if __name__=="__main__":
    if len(sys.argv)==2:
        init(sys.argv[1])
    else:
        print('error: arg is too much or less')

