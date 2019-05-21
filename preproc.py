from tika import parser
from konlpy.tag import Kkma
from hanspell import spell_checker
import re

def init(path):
    text=parser.from_file(path)
    text = delete_newline(text['content'])
    sentence=sentences(text)
    delete_index(sentence)
    spell_check(sentence)
    fp=open("./nonmun6.txt",'w')
    print(sentence,file=fp)
    return sentence
#     path=path[0:len(path)-4]+".txt"
#     fp=open(path,'w',encoding='utf-8')
#     print(sentence,file=fp)
#     fp.close()
    
# def getText(text):
#     sentences=sentences(text)
#     text= ""
#     with open(path,encoding='utf=8') as fp:
#         while True:
#             line = fp.readline()
#             if not line:
#                 break
#             else:
#                 text=text+line
#     fp.close()
#     return text

def spell_check(sentence):
    print(len(sentence))
    pattern=re.compile(' |-\d*-')
    pattern2=re.compile('-\d*-')
    for idx in range(len(sentence)):
        sentence[idx]=re.sub(pattern,'',sentence[idx])
        sentence[idx]=re.sub(pattern2,'',sentence[idx])
        result=spell_checker.check(sentence[idx])
        sentence[idx]=result.checked.replace(u'\xa0','')
    print(len(sentence))
    
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
    init("./nonmun.pdf")
#     text=sentences("./result.txt")
#     print(text)
