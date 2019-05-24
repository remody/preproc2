{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from tika import parser\n",
    "import re\n",
    "import sys\n",
    "import json\n",
    "\n",
    "def delete_newline(text):\n",
    "    pattern=re.compile('\\n')\n",
    "    text=re.sub(pattern,'',text)\n",
    "    return text\n",
    "\n",
    "def elastic(path):\n",
    "    data = {}\n",
    "    text= parser.from_file(path)\n",
    "    pattern= re.compile('- \\d* -')\n",
    "    text= delete_newline(text['content'])\n",
    "    text= re.sub(pattern,'',text)\n",
    "    length=(len(text)//15000)+1\n",
    "    for idx in range(length):\n",
    "        if idx ==length-1:\n",
    "            data[idx]=text[idx*15000:]\n",
    "        else:\n",
    "            data[idx]=text[(idx)*15000:(idx+1)*15000]\n",
    "    path=path[0:len(path)-4]+'_elastic'+\".json\"\n",
    "    fp=open(path,'w')\n",
    "    json.dump(data,fp,ensure_ascii=False)\n",
    "    fp.close()\n",
    "    \n",
    "if __name__==\"__main__\":\n",
    "#     elastic(sys.argv[1])\n",
    "    elastic('./nonmun.pdf')\n"
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
