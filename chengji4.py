#_*_encoding:cp936_*_
import random
from openpyxl import load_workbook
wb = load_workbook(r'c:\users\administrator\desktop\name.xlsx')
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
    while i<=num and num<=len(l):
        print random.choice(lists)
        i = i + 1
nums = ws.max_row
while 1>0 :
    if i == 1 :
        print('')
        n = input('               �����뿼�Ų�ѯ��')
        for i in range(2,nums) :
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
            else :
                pass
    elif i == 2 :
        print('')
        m = input('               �����뿼�Ų�ѯ��')
        for i in range(2,nums) :
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
    elif i == 3 :
        print('')
        print('  δ���£��޷���ʾ')
    elif i == 4 :
        print('')
        print('  �߶��ӳٿ�ѧ����ѧʱ������֪ͨ��')
    elif i == 5 :
        print('')
        print('               ================================')
        print('               |�ɼ���ѯ���v4.4              |')
        print('               |                              |')
        print('               |�������������                |')
        print('               |                              | ')
        print('               |�������ʱ�䣺2020.1.29 19:31 |')
        print('               ================================')
    elif i == 6 :
        pass
        '''q = input('               ������Ҫѡ���������')        
        choice(l,q)'''    
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
    else :
        print('               ������Ϸ��ַ�!')
        continue
    i = input('               �밴�¶�Ӧ����ѡ��') 
      
