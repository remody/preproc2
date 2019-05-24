{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "269\n",
      "269\n"
     ]
    }
   ],
   "source": [
    "from tika import parser\n",
    "from konlpy.tag import Kkma\n",
    "from hanspell import spell_checker\n",
    "import re\n",
    "from PyPDF2 import PdfFileReader\n",
    "from pdfrw import PdfReader\n",
    "import sys\n",
    "import json\n",
    "\n",
    "def init(path):\n",
    "    text=parser.from_file(path)\n",
    "    text = delete_newline(text['content'])\n",
    "    sentence=sentences(text)\n",
    "    delete_index(sentence)\n",
    "    spell_check(sentence)\n",
    "    path=path[0:len(path)-4]+\".txt\"\n",
    "    fp=open(path,'w')\n",
    "    data={'sentence':sentence}\n",
    "    print(data,file=fp)\n",
    "    fp.close()\n",
    "    \n",
    "# def getText(text):\n",
    "#     sentences=sentences(text)\n",
    "#     text= \"\"\n",
    "#     with open(path,encoding='utf=8') as fp:\n",
    "#         while True:\n",
    "#             line = fp.readline()\n",
    "#             if not line:\n",
    "#                 break\n",
    "#             else:\n",
    "#                 text=text+line\n",
    "#     fp.close()\n",
    "#     return text\n",
    "\n",
    "def spell_check(sentence):\n",
    "    print(len(sentence))\n",
    "    pattern=re.compile(' ')\n",
    "    pattern2=re.compile('-\\d*-')\n",
    "    for idx in range(len(sentence)):\n",
    "        sentence[idx]=re.sub(pattern,'',sentence[idx])\n",
    "        sentence[idx]=re.sub(pattern2,'',sentence[idx])\n",
    "        result=spell_checker.check(sentence[idx])\n",
    "        sentence[idx]=result.checked.replace(u'\\xa0','')\n",
    "    print(len(sentence))\n",
    "    \n",
    "def delete_newline(text):\n",
    "    pattern=re.compile('\\n')\n",
    "    text=re.sub(pattern,'',text)\n",
    "    return text\n",
    "\n",
    "def sentences(text):\n",
    "    kkma=Kkma()\n",
    "    sentence=kkma.sentences(text)\n",
    "    del kkma\n",
    "    return sentence\n",
    "\n",
    "def delete_index(sentence):\n",
    "    r=re.compile(\"목차|목 차\")\n",
    "    for idx in range(len(sentence)):\n",
    "        if r.search(sentence[idx]) is not None:\n",
    "            del sentence[idx]\n",
    "            break \n",
    "if __name__==\"__main__\":\n",
    "#     init(sys.argv[1])\n",
    "    init('./nmg.pdf')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
