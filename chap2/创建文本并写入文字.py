fp=open("note.txt","w")#创建文本
print("北京欢迎你！",file=fp)#写入到note.txt文件中
fp.close()#关闭文件