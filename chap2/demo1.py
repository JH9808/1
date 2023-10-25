print("Hello,world2!")
a = 100
b = 50
print(a)
print(b)
print(a*b)
print(a/b)
print("北京欢迎你！")
print(a, b, "Hello world!")
print(a,b,"Hello world")
print("b")
print(chr(98))#使用chr()将98转换成ASCII表中的字符
print("C")
print(chr(67))
fp=open("note.txt","w")#创建文本
print("北京欢迎你！",file=fp)#写入到note.txt文件中
fp.close()#关闭文件
print("北京",end="-->")
print("欢迎你")
print("Hello Python world!")
message = "Hello Python world!"
print(message)

message = "Hello Python Course world!"
print(message)
print("massage")
fp=open("text.txt","w")
print("人生苦短，我用Python",file=fp)
fp.close()