#_*_encoding:cp936_*_
import random
print('��ӭʹ�óɼ���ѯ���')
print('*********************')
print('1 �ɼ���ѯ')
print('2 ѧ���༶��ѯ')
print('3 ѧУ�γ̱�')
print('4 ѧУ����')
print('5 ����汾��Ϣ')
print('6 ���ѡȡ')
print('7 �˳�')
print('*********************')
i = input('�밴�¶�Ӧ����ѡ��')
p = ['����',101010,'����14',100,100,100,100,100,100,600]
h = ['����',202020,'����14',100,100,100,100,100,100,600]
l = ['��һ','�¶�','����','����','����','����','����','�ܰ�','���','֣ʮ']
def choice(lists,num):
    i = 1
    while i<=num and num<=len(l):
        print random.choice(lists)
        i = i + 1

while 1>0 :
    if i == 1 :
        n = input('�����뿼�Ų�ѯ��')
        if n == p[1] :
            print('======�ɼ�=======')
            print('|������{}      |'.format(p[0]))
            print('|���ţ�{}    |'.format(p[1]))
            print('|�༶��{}    |'.format(p[2]))
            print('|���ģ�{}       |'.format(p[3]))
            print('|��ѧ��{}       |'.format(p[4]))
            print('|Ӣ�{}       |'.format(p[5]))
            print('|����{}       |'.format(p[6]))
            print('|��ѧ��{}       |'.format(p[7]))
            print('|���{}       |'.format(p[8]))
            print('|�ܷ֣�{}       |'.format(p[9]))
            print('=================')   
        elif n == h[1] :
            print('======�ɼ�=======')
            print('|������{}      |'.format(h[0]))
            print('|���ţ�{}    |'.format(h[1]))
            print('|�༶��{}    |'.format(h[2]))
            print('|���ģ�{}       |'.format(h[3]))
            print('|��ѧ��{}       |'.format(h[4]))
            print('|Ӣ�{}       |'.format(h[5]))
            print('|����{}       |'.format(h[6]))
            print('|��ѧ��{}       |'.format(h[7]))
            print('|���{}       |'.format(h[8]))
            print('|�ܷ֣�{}       |'.format(h[9]))
            print('=================')
    elif i == 2 :
        m = input('�����뿼�Ų�ѯ��')
        if m == p[1] :
            print('====ѧ����Ϣ=====')
            print('|������{}      |'.format(p[0]))
            print('|���ţ�{}    |'.format(p[1]))
            print('|�༶��{}    |'.format(p[2]))
            print('=================')
        elif m == h[1] :
            print('======�ɼ�=======')
            print('|������{}      |'.format(h[0]))
            print('|���ţ�{}    |'.format(h[1]))
            print('|�༶��{}    |'.format(h[2]))
            print('=================')
    elif i == 3 :
        print('δ���£��޷���ʾ')
    elif i == 4 :
        print('�߶��ӳٿ�ѧ����ѧʱ������֪ͨ��')
    elif i == 5 :
        print('===============================')
        print('�ɼ���ѯ���v3.0')
        print('�������������')
        print('�������ʱ�䣺2020.1.28 19:18')
        print('===============================')
    if i == 6 :
        q = input('������Ҫѡ���������')        
        choice(l,q)
    print('**********************')
    print('1 �ɼ���ѯ')
    print('2 �༶��ѯ')
    print('3 ѧУ�γ̱�')
    print('4 ѧУ����')
    print('5 ����汾��Ϣ')
    print('6 ���ѡȡ')
    print('7 �˳�')
    print('**********************')
    i = input('�밴�¶�Ӧ����ѡ��')  
    if i == 7 :
        print('****��ӭʹ�óɼ���ѯ���****')
        break
      
