#_*_encoding:cp936_*_
import random
from openpyxl import load_workbook
wb = load_workbook(r'F:\����\name.xlsx')
ws = wb.active
print('')
print('')
print('                          ��ӭʹ�óɼ���ѯ���')
print('')
print('1 �ɼ���ѯ        '),
print('2 �༶��ѯ      '),
print('3 ѧУ�γ̱�   '),
print('4 ѧУ����     ')
print('')
print('5 ����汾��Ϣ    '),
print('6 ���ѡȡ      '),
print('7 �˳�')
print('')
i = input('               �밴�¶�Ӧ����ѡ��')
def choice(lists,num):
    i = 1
    while i<=num and num<=len(lists):
        print('               ')
        print random.choice(lists)
        i = i + 1
def kaohao(n) :
    ceshi = 0
    nums = ws.max_row
    for i in range(2,nums+1) :
        if n == ws.cell(row=i,column=1).value :
            print('')
            print('               =================')
            print('               | ������'),
            print(ws.cell(row=i,column=2).value),
            print('  |')
            print('               |               | ')
            print('               |���ţ�{}  |'.format(ws.cell(row=i,column=1).value))
            print('               |               | ')
            print('               ======�ɼ�=======')
            print('               |���ģ�{}       |'.format(ws.cell(row=i,column=3).value))
            print('               |��ѧ��{}       |'.format(ws.cell(row=i,column=4).value))
            print('               |Ӣ�{}       |'.format(ws.cell(row=i,column=5).value))
            print('               |����{}       |'.format(ws.cell(row=i,column=6).value))
            print('               |��ѧ��{}       |'.format(ws.cell(row=i,column=7).value))
            print('               |���{}       |'.format(ws.cell(row=i,column=8).value))
            print('               |�ܷ֣�{}      |'.format(ws.cell(row=i,column=10).value))
            print('               =================')
            ceshi = 1
        else :
            pass
    if ceshi == 0 :
        print('')
        print('               ���Ŵ���')
        print('')
        n = input('               ���������뿼�Ų�ѯ��2���أ�')
        if n != 2 :
            kaohao(n)
        else :
            pass
        
def xinxi(m) :
    ceshi = 0
    nums = ws.max_row
    for i in range(2,nums+1) :
        if m == ws.cell(row=i,column=1).value :

            print('')
            print('               ====ѧ����Ϣ=====')
            print('               | ������'),
            print(ws.cell(row=i,column=2).value),
            print('  |')
            print('               |               | ')
            print('               |���ţ�{}  |'.format(ws.cell(row=i,column=1).value))
            print('               |               |')
            print('               |�༶��'),
            print(ws.cell(row=i,column=11).value),
            print('  |')
            print('               =================')
            ceshi = 1
        else :
            pass
    if ceshi == 0 :
        print('')
        print('               ���Ŵ���')
        print('')
        n = input('               ���������뿼�Ų�ѯ��2���أ�')
        if n != 2 :
            xinxi(m)
        else :
            pass

nums = ws.max_row

while 1>0 :
    
    if i == 1 :
        print('')
        n = input('               �����뿼�Ų�ѯ��')
        kaohao(n)
        
    elif i == 2 :
        print('')
        m = input('               �����뿼�Ų�ѯ��')
        xinxi(m)
        
    elif i == 3 :
        print('')
        print('  δ���£��޷���ʾ')
        
    elif i == 4 :
        print('')
        print('  �߶��ӳٿ�ѧ����ѧʱ������֪ͨ��')
        
    elif i == 5 :
        print('')
        print('               ================================')
        print('               |�ɼ���ѯ���v5.3              |')
        print('               |                              |')
        print('               |�������������                |')
        print('               |                              | ')
        print('               |�������ʱ�䣺2020.1.30 12:31 |')
        print('               ================================')
        
    elif i == 6 :
        l = []
        nums = ws.max_row        
        for p in range(2,nums) :
            names = ws.cell(row = p,column=2).value
            l.append(names)
            p = p + 1
        print('')
        q = input('               ������Ҫѡ���������')        
        choice(l,q)
        
    elif i == 7 :
        print('')
        print('               ****��ӭʹ�óɼ���ѯ���****')
        break
    else :
        print('')
        print('               ������Ϸ��ַ�!')
        
    print('')
    print('               1 ����    '),
    print('2 �˳�')
    print('')

    c = input('               �Ƿ������')
    
    while c != 1 and c != 2 :
        print('')
        print('               ������Ϸ��ַ�!')
        print('')
        print('               1 ����    '),
        print('2 �˳�')
        print('')
        c = input('               �Ƿ������')
    if c == 1 :
        print('')
        print('1 �ɼ���ѯ        '),
        print('2 �༶��ѯ      '),
        print('3 ѧУ�γ̱�   '),
        print('4 ѧУ����     ')
        print('') 
        print('5 ����汾��Ϣ    '),
        print('6 ���ѡȡ      '),
        print('7 �˳�')
        print('')     
    elif c == 2 :
        break
    
    i = input('               �밴�¶�Ӧ����ѡ��')       
