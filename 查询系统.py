#_*_encoding:cp936_*_
import random
print('欢迎使用成绩查询软件')
print('*********************')
print('1 成绩查询')
print('2 学生班级查询')
print('3 学校课程表')
print('4 学校公告')
print('5 软件版本信息')
print('6 随机选取')
print('7 退出')
print('*********************')
i = input('请按下对应数字选择：')
p = ['潘正',101010,'二·14',100,100,100,100,100,100,600]
h = ['韩旭',202020,'二·14',100,100,100,100,100,100,600]
l = ['刘一','陈二','张三','李四','王五','赵六','孙七','周八','吴九','郑十']
def choice(lists,num):
    i = 1
    while i<=num and num<=len(l):
        print random.choice(lists)
        i = i + 1

while 1>0 :
    if i == 1 :
        n = input('请输入考号查询：')
        if n == p[1] :
            print('======成绩=======')
            print('|姓名：{}      |'.format(p[0]))
            print('|考号：{}    |'.format(p[1]))
            print('|班级：{}    |'.format(p[2]))
            print('|语文：{}       |'.format(p[3]))
            print('|数学：{}       |'.format(p[4]))
            print('|英语：{}       |'.format(p[5]))
            print('|物理：{}       |'.format(p[6]))
            print('|化学：{}       |'.format(p[7]))
            print('|生物：{}       |'.format(p[8]))
            print('|总分：{}       |'.format(p[9]))
            print('=================')   
        elif n == h[1] :
            print('======成绩=======')
            print('|姓名：{}      |'.format(h[0]))
            print('|考号：{}    |'.format(h[1]))
            print('|班级：{}    |'.format(h[2]))
            print('|语文：{}       |'.format(h[3]))
            print('|数学：{}       |'.format(h[4]))
            print('|英语：{}       |'.format(h[5]))
            print('|物理：{}       |'.format(h[6]))
            print('|化学：{}       |'.format(h[7]))
            print('|生物：{}       |'.format(h[8]))
            print('|总分：{}       |'.format(h[9]))
            print('=================')
    elif i == 2 :
        m = input('请输入考号查询：')
        if m == p[1] :
            print('====学生信息=====')
            print('|姓名：{}      |'.format(p[0]))
            print('|考号：{}    |'.format(p[1]))
            print('|班级：{}    |'.format(p[2]))
            print('=================')
        elif m == h[1] :
            print('======成绩=======')
            print('|姓名：{}      |'.format(h[0]))
            print('|考号：{}    |'.format(h[1]))
            print('|班级：{}    |'.format(h[2]))
            print('=================')
    elif i == 3 :
        print('未更新，无法显示')
    elif i == 4 :
        print('高二延迟开学，开学时间另行通知。')
    elif i == 5 :
        print('===============================')
        print('成绩查询软件v3.0')
        print('软件制作：韩旭')
        print('软件制作时间：2020.1.28 19:18')
        print('===============================')
    if i == 6 :
        q = input('请输入要选择的人数：')        
        choice(l,q)
    print('**********************')
    print('1 成绩查询')
    print('2 班级查询')
    print('3 学校课程表')
    print('4 学校公告')
    print('5 软件版本信息')
    print('6 随机选取')
    print('7 退出')
    print('**********************')
    i = input('请按下对应数字选择：')  
    if i == 7 :
        print('****欢迎使用成绩查询软件****')
        break
      
