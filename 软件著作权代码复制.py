#coding=gbk

import os

# ����ļ�
outFile = "C:\\Users\\Hxuejie\\Desktop\outFile.txt"
# ��ĿĿ¼
proDir = "C:\\Users\\Hxuejie\\Documents\\Projects\\Web\\oa_29"

# д��Ŀ¼�µ������ļ�
# �����ļ�����
def writeDir(d):
    count = 0
    fs = os.listdir(d)
    for f in fs:
        p = d + "/" + f
        if os.path.isdir(p):
            count += writeDir(p)
        else:
            writeFile(p)
            count += 1
    return count
    

# д���ļ�
def writeFile(f):
    if not f.endswith(".java"):
        return
    rf = open(f)
    for l in rf:
        __of.write(l)
    rf.close()
    return

# ɾ��ע��
def delComment():
    __of.seek(0,0)
    __of_co = open(outFile + ".co", "a+")
    multiline = False
    count = 0
    for l in __of:
        if l.lstrip().startswith("/*"): # ����ע��
            multiline = True
            count += 1
            continue
        if l.rstrip().endswith("*/"):
            multiline = False
            count += 1
            continue
        if multiline:
            count += 1
            continue
        if l.lstrip().startswith("//"): # ����ע��
            count += 1
            continue
        if l.isspace(): # ����
            continue
        __of_co.write(l)
    __of_co.close()
    return count

# ִ��д��
print "=================��ʼд��=================="
print "������Ŀ��", proDir
print "����ļ���", outFile
__of = open(outFile, "a+")
count = writeDir(proDir)
print "д���ļ�������", count
count = delComment()
print "ɾ��ע��������", count
__of.close()
print "=================д�����=================="

