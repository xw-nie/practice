# coding:cp936

import os
def search(key,address):
    file_list = []
    for path,dirnames,filenames in os.walk(address):
        print('search'+path+'...')
        for name in filenames:
            if key in name:
                file_list.append(path+'\\'+ name)
            '''
            with open(path+'\\'+name)as f :
                for l in f :
                    if key in l :
                        file_list.append(path+'\\'+ name+':'+l)\\\
                        '''
    return file_list
kw = input('search:')
ad = input('in:')
if not ad.strip():
    ad = '.'
for i in search(kw,ad):
    print(i)
#备注