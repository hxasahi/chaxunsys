#_*_encoding:cp936_*_
import random

l = ['��','��','��','��','��','��','��','��','��','��','��','Ǯ','֣','��','��','��','��','��','��']

def choice(lists,num):
    i = 1
    while i<=num and num<=len(l):
        print random.choice(lists)
        i = i + 1

n = input('������Ҫѡ���������')        

choice(l,n)
