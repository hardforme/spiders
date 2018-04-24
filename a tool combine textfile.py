# -*- coding:utf-8 -*-
import os

def get_txt(path):
    fnames = os.listdir(path)
    txtlist = []
    for fname in fnames:
        if fname[-4:]=='.txt':
            fullname = path + '\\' + fname.decode('gbk')
            #print fullname, '\n'
            txtlist.append(fullname)
    if len(txtlist)==0:
        print 'there are not text file in this file:' + path + '\n'
        return None
    else:
        cb_f_name = path + '\\' + os.path.split(path)[1] + '.txt'
        cb_f = open(cb_f_name, 'a+')
        for i in range(len(txtlist)):
            if cb_f_name == txtlist[i]:
                continue
            f = open(txtlist[i], 'r')
            combine(cb_f, i+1, f)
            f.close()
    cb_f.close()

def combine(cb_f, order, f):
    #print os.path.split(f.name)
    title = 'NO.'+str(order)+':'+os.path.split(f.name)[1]+'\n'
    print title
    cb_f.write(title.encode('gbk'))
    f_read = f.read().decode('utf-8').encode('gb18030')
    try :
        cb_f.write(f_read+'\n')
    except:
        print 'can\'t write', title

for i in range(1,10):
    if i==1:
        get_txt('F:\\porn\\text\\xiaoyuan')
        continue
    son_fname = 'index_'+str(i)+'.htm'
    get_txt('F:\\porn\\text\\xiaoyuan'+'\\'+son_fname)
