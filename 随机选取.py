#_*_encoding:cp936_*_
import random

l = ['��һ','�¶�','����','����','����','����','����','�ܰ�','���','֣ʮ']

def choice(lists,num):
    i = 1
    while i<=num and num<=len(lists):
        print random.choice(lists)
        i = i + 1

n = input('������Ҫѡ���������')        

choice(l,n)
