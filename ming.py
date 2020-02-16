#_*_encoding:cp936_*_
import random

l = ['项','万','福','侠','心','海','康','宁','冲','元','云','飞','风','峰','贵','国','雪','夏','霞']

def choice(lists,num):
    i = 1
    while i<=num and num<=len(l):
        print random.choice(lists)
        i = i + 1

n = input('请输入要选择的人数：')        

choice(l,n)
