# -*- coding: utf-8 -*-
import urllib.request, re
from urllib.request import urlopen

dic = {}
link = 'http://www.dil.ie/35842'
test = urllib.request.urlopen(link)
p = test.read()

page = open('page.txt', 'w')
page.write(str(p))
page.close()

page_test = open('page.txt')
for line in page_test:
    t = re.findall(r'headword_id="(?:[0-9]*[a-z]*)"[>\\n]*(.*?)</h3>', line)
    s = re.findall(r'Forms[>:]*[>\\n]*[\s*]*[>\\t]*[\s*]*(.*?)</p>', line)
    dic["Источник: " + link + "\nИрландское слово: " + ''.join(t)] = "Формы: " + ''.join(s)

def Dictionar(dict, filename, sep):
    with open(filename, "a") as f:
        for i in dict.keys(): 
            f.write(i + " " + sep.join([str(x) for x in dict[i]]) + "\n")

Dictionar(dic, 'dictionary_page', '')
