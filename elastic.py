#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tika import parser
import re
import sys
import json
import os

def delete_newline(text):
    pattern=re.compile('\n')
    text=re.sub(pattern,'',text)
    return text

def elastic(argv):
    data = {}
    os.rename(argv[1],'temp.pdf')
    
    jsonpath=argv[1][0:len(argv[1])-4]"_elastic"+".json"
    pathlist=argv[1].split('/')
    pathlist[len(pathlist)-1]='temp.pdf'
    pdfpath='/'.join(pathlist)
    
    text= parser.from_file(pdfpath)
    
    pattern= re.compile('- \d* -')
    text= delete_newline(text['content'])
    text= re.sub(pattern,'',text)
    if sys.getsizeof(text)>31999:
        print("NO")
        return
    data["body"]=text
    data["title"]=argv[2]
    data["creator"]=argv[3]
    data["belong"]=argv[4]
    data["data"]=argv[5]
    fp=open(jsonpath,'w')
    json.dump(data,fp,ensure_ascii=False)
    fp.close()
    os.remove(pdfpath)
    print("YES")
    
if __name__=="__main__":
    if len(sys.argv) == 6:
        elastic(sys.argv)
    else:
        print('Error : check your arg')

