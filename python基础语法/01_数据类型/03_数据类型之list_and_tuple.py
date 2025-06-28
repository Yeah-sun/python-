# ### 列表类型 list

#定义一个空的list
listvar = []
print(listvar)

#定义普通列表
listvar = ["asa",222,2.2,12-3j]

#获取列表中的元素
#正向索引
print(listvar[1])
#逆向索引
print(listvar[-3])

#修改列表中的元素
listvar[1] = "大象"
print(listvar)

# ### tuple类型
tuplevar = (1,2,3,"sss")
print(tuplevar)

#获取tuple中的元素
print(tuplevar[1])
print(tuplevar[-1])

# tuplevar[1] = "wm" 会报错

# 注意:
""" 逗号才是区分元组的标识符 """
tuplevar = (1)
print(type(tuplevar))
tuplevar = (1,)
print(type(tuplevar))
#定义一个空元组
tuplevar = ()
print(type(tuplevar))



