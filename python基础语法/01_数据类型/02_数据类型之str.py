# ### 字符串类型 str
'''
用引号引起来的就是字符串,单引号,双引号,三引号

# 转义字符  \ + 字符
    (1) 可以将无意义的字符变得有意义
    (2) 可以将有意义的字符变得无意义
常见的几种:
\n      : 换行
\r\n    : 换行(Windows系统中常用\r\n表示行结束符)
\t      : 缩进(水平制表符)
\r      : 将\r后的字符串拉到当前行的行首
'''

# 1. 单引号的字符串
strvar = '生活不止眼前的苟且'
print(strvar,type(strvar))

# 2. 双引号的字符串
strvar = "还有诗和远方的田野"
print(strvar,type(strvar))
## 可以将无意义的字符变得有意义
strvar = "还有诗和\n远方的田野"
strvar = "还有诗和\r\n远方的田野"
strvar = "还有诗和\t远方的田野"
strvar = "还有诗和\r远方的田野"
strvar = "还有诗和\n远方的\r田野"
## 可以将有意义的字符变得无意义
strvar = "还有诗和\"远方\"的田野"
print(strvar,type(strvar))

# 3. 三引号的字符串(支持跨行效果)
strvar = '''
我真的很无奈
你怎么专门能吃
'''
print(strvar,type(strvar))

# 4. 原(raw)字符串:r"字符串"  原型化输出字符串(这个可以避免歧义,减少操作)
strvar = "D:\ndadas\tdadasda\radsasd"
strvar = r"D:\ndadas\tdadasda\radsasd"
print(strvar,type(strvar))

# 5. 字符串的格式化
'''
%d 整数占位符
%f 浮点数占位符
%s 字符串占位符
语法格式:
   "字符串" %(值1,值2)
'''
## %d 整型占位符
strvar = "一个星期有%d" %(7)
### %2d  右对齐占俩位
strvar = "一个星期有%2d" %(7)
### %-2d 左对齐占俩位
strvar = "一个星期有%-2d" %(7)
print(strvar,type(strvar))

## %f 浮点数占位符(默认保留6位)
strvar = "我存款有%f元" %(10000.235)
### %.2f 保留小数点后俩位(四舍五入)
strvar = "我存款有%.2f元" %(10000.235)
print(strvar,type(strvar))

## %s 字符串占位符
strvar = "我觉得%s喜欢%s"% ("小明","小红")
print(strvar,type(strvar))

#综合案例:
strvar = "我觉得%s喜欢%s,因为小红存款有%.2f万,一个星期有%s天"% ("小明","小红",10000.235,7)
print(strvar,type(strvar))

## 当你不知道对面说明类型是可以都使用字符串占位符
strvar = "我觉得%s喜欢%s,因为小红存款有%s万,一个星期有%s天"% ("小明","小红",10000.235,7)