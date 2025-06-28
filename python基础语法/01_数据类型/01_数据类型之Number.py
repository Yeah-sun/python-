# ### Number数字类型 (int float bool complex)

################################################################################
print("int整型:")
# int 整形 (正整数 0 负整数)

intvar = 100
print(intvar)

# type 获取值的类型
res = type(intvar)
print(res)

# id 获取值的地址
res = id(intvar)
print(res)

# 二进制整型
intvar = 0b110
print(intvar)
print(type(intvar))
print(id(intvar))    #运行这串代码,这里学过c的都看出来了,它改变的不是原本地址的值,也验证了C语言的变量与python的区别

# 八进制整型
intvar = 0o127
print(intvar)
print(type(intvar))
print(id(intvar))

# 十六进制整型
intvar = 0xfff
print(intvar)
print(type(intvar))
print(id(intvar))

'''
二进制 1+1 = 10
八进制 7+1 = 10
十六进制 f+1 = 10
'''
#############################################################################
# float 浮点数(小数)
print("float浮点型:")

# 表示方法1
floatvar = 3.6
print(floatvar,type(floatvar))
# 表示方法2
floatvar = 5.7e5 # 5.7*10的5次方
floatvar = 5.6e-2 # 5.7*10的-2次方
print(floatvar,type(floatvar))

###################################################################################
# bool 布尔型(True Flase)
print("bool类型:")
boolvar = True
print(boolvar,type(boolvar))

#####################################################################################
# complex 复数类型
print("complex 复数类型:")
'''
3+4j
实数+虚数
实数:3
虚数:4j
'''
# 表达方式1:
complexvar = 3 + 4j
complexvar = -3j
print(complexvar,type(complexvar))
# 表达方式2:
res = complex(3,4)
print(res,type(res))
'''
类型转换机制
自动转换：Python会在特定情况下自动进行数字类型转换
转换规则：
低精度类型会自动向高精度类型转换
转换顺序：bool → int → float → complex
'''