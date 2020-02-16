#_*_encoding:cp936_*_
import random

l = ['张','刘','赵','宣','潘','韩','程','李','邵','孙','苏','钱','郑','单','马','陈','周','于','徐']

def choice(lists,num):
    i = 1
    while i<=num and num<=len(l):
        print random.choice(lists)
        i = i + 1

n = input('请输入要选择的人数：')        

choice(l,n)
