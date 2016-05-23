# -*- coding: utf-8 -*-

import os, sys
import json
import hashlib
import urllib.request, urllib.parse
import simplejson as json
import codecs   # используется для открытия utf-8 файлов
root_path = './@Сайт'
root_url = 'http://127.0.0.1:5000/'
d = os.listdir(root_path)
  
def update_teachers(controller, action):
    teachers = {}
    for f in d:
        print(root_path+'/'+f)
        if os.path.isdir(root_path+'/'+f):
            if not os.path.exists(root_path+'/'+f+'/descr.txt'):
                continue
            teachers[f] = {'Name':'', 'Photo':{'FileName':'', 'MD5':''}, 'Descr':''}
            try:
                fDescr = codecs.open(root_path+'/'+f+'/descr.txt','r', 'utf-8')
                fio = fDescr.readline() # читаем первую строку, чтобы поймать/не поймать ошибку
            except UnicodeDecodeError:
                fDescr = codecs.open(root_path+'/'+f+'/descr.txt', 'r')
                fio = fDescr.readline() # записываем корректные данные переменной в случае ошибки
            descr = fDescr.readline()
            disciplines = fDescr.readline()
            teachers[f]['Name'] = fio
            teachers[f]['Descr'] = descr
            teachers[f]['Photo']['FileName'] = root_path+'/'+f+'/фото.jpg'
            teachers[f]['Photo']['MD5'] = hashlib.md5(open(teachers[f]['Photo']['FileName'],'rb').read()).hexdigest()
            teachers[f]['Disciplines'] = disciplines

    values = {'Data':json.dumps(teachers), 'Command':'UpdateTeachers'}
    data = urllib.parse.urlencode(values).encode("utf-8")
    url = root_url + controller + action
    print(url)
    f = urllib.request.urlopen(url, data = data)
    # print(f.read())
    
def update_disciplines(controller, action):
    try:
        disciplines = codecs.open(root_path+"/disciplines.json", "r", 'utf-8')
        disciplines = disciplines.read() # читаем первую строку, чтобы поймать/не поймать ошибку
    except UnicodeDecodeError:
        fDescr = codecs.open(root_path+'/'+f+'/disciplines.json', 'r')
        disciplines = disciplines.read() # читаем первую строку, чтобы поймать/не поймать ошибку
    values = {'Data':disciplines, 'Command':'UpdateDisciplines'}
    data = urllib.parse.urlencode(values).encode('utf-8')
    url = root_url + controller + action
    print(url)
    f = urllib.request.urlopen(url, data = data)
    # print(f.read())

''' Main '''

if "-ut" in sys.argv:
    update_teachers("test", "")

elif "-ud" in sys.argv:
    update_disciplines("test", "")