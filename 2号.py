# -*- coding: cp936 -*-
from openpyxl import load_workbook
wb = load_workbook(r'c:\users\administrator\desktop\name.xlsx')
ws = wb.active
n = input('�����뿼�Ų�ѯ��')
num = ws.max_row
for i in range(2,num) :
    if n == ws.cell(row=i,column=1).value :
        print('=================')
        print(' ������'),
        print(ws.cell(row=i,column=2).value)
        print('======�ɼ�=======')
        print('|���ģ�{}       |'.format(ws.cell(row=i,column=3).value))
        print('|��ѧ��{}       |'.format(ws.cell(row=i,column=4).value))
        print('|Ӣ�{}       |'.format(ws.cell(row=i,column=5).value))
        print('|����{}       |'.format(ws.cell(row=i,column=6).value))
        print('|��ѧ��{}       |'.format(ws.cell(row=i,column=7).value))
        print('|���{}       |'.format(ws.cell(row=i,column=8).value))
        print('|�ܷ֣�{}      |'.format(ws.cell(row=i,column=10).value))
        print('=================')
