#_*_encoding:cp936_*_
import cv2
import numpy as np
import os
import random
from openpyxl import load_workbook
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('               1 ����ʶ��'),
print('               2 �˺�����')
print('')
xxx=input('               ��ѡ���¼��ʽ��') 


while xxx==2:
    print('')
    name=raw_input('               �������˺�����')
    print('')
    password=raw_input('               ���������룺')
    break

while xxx==1:
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('F:/trainer/trainer.yml')
    cascadePath = "C:/Python27/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
 
    font = cv2.FONT_HERSHEY_SIMPLEX
 
    #iniciate id counter
    id = 0
    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height
 
    ret, img =cam.read()
    img = cv2.flip(img, 1) # Flip vertically
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # names related to ids: example ==> Marcelo: id=1,  etc
    names = ['None', 'Hx', 'Mom', 'None', 'None', 'None'] 
 

    
    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
     
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
 
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
 
        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 50):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
         
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
     
    cv2.imshow('camera',img)
    
 
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if id == 'Hx' :
        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()

        break
 
    
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

while id == 'Hx' or (name == 'Hx' and password == '0824' ):
    
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
        print('               |�ɼ���ѯ���v6.1              |')
        print('               |                              |')
        print('               |�������������                |')
        print('               |                              | ')
        print('               |�������ʱ�䣺2020.2.12 16:40 |')
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

