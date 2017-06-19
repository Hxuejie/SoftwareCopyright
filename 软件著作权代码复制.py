#coding=gbk

import os

# 输出文件
outFile = "C:\\Users\\Hxuejie\\Desktop\outFile.txt"
# 项目目录
proDir = "C:\\Users\\Hxuejie\\Documents\\Projects\\Web\\oa_29"

# 写入目录下的所有文件
# 返回文件总数
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
    

# 写入文件
def writeFile(f):
    if not f.endswith(".java"):
        return
    rf = open(f)
    for l in rf:
        __of.write(l)
    rf.close()
    return

# 删除注释
def delComment():
    __of.seek(0,0)
    __of_co = open(outFile + ".co", "a+")
    multiline = False
    count = 0
    for l in __of:
        if l.lstrip().startswith("/*"): # 多行注释
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
        if l.lstrip().startswith("//"): # 间行注释
            count += 1
            continue
        if l.isspace(): # 空行
            continue
        __of_co.write(l)
    __of_co.close()
    return count

# 执行写入
print "=================开始写入=================="
print "输入项目：", proDir
print "输出文件：", outFile
__of = open(outFile, "a+")
count = writeDir(proDir)
print "写入文件总数：", count
count = delComment()
print "删除注释总数：", count
__of.close()
print "=================写入完成=================="

