#_*_encoding:cp936_*_
import random

l = ['刘一','陈二','张三','李四','王五','赵六','孙七','周八','吴九','郑十']

def choice(lists,num):
    i = 1
    while i<=num and num<=len(lists):
        print random.choice(lists)
        i = i + 1

n = input('请输入要选择的人数：')        

choice(l,n)
