# # while 条件循环
# i =1
# while i <=3:
#     print("好好学习，天天向上")
#     i=i+1
# while 死循环
# while true
#for i in range (1,9):
	# print(i)


#     # 字符串查找，判断，修改

# 字符串查找：                  在python中，字符串查找，判断，修改可以将字符串结束下标超过字符串长度，越界不会报错：对于 start:end 这种切片范围，超出部分被自动忽略。 只要 start 在合法范围内，end 大于长度就等同于直接取到字符串末尾。如果 end 是负数，Python 会先计算 len(s) + end，如果结果仍超出范围，同样会自动截断（例如 s[0:-100] 会返回空字符串 ""）。
#     find：检测子字符是否包含在字符串中,如果在就返回这个字符串开始位置的下标，否则就返回-1
#         格式：str.find(sub,start=0,end=len(str))   sub:要查找的字符串，start：可选，查找起始下标，从start开始，默认0，end，可选，查找结束的下标(不包含)
# name = "tanhaitian1111"
# print(name.find("a"))   返回1
# print(name.find("an"))  返回1
# print(name.find("a",2,5))   返回4
# print(name.find("a",9,13))  无论超过或者不被包含，都返回-1
#         index:规则与find一致，只不过find不被包含则返回-1，而index会直接报错
# name = "tanhaitian1111"
# print(name.index("a"))
# print(name.index("a",16),)超出范围，直接报错

#         conut():返回某个子字符串在整个字符串中出现的次数，没有就返回0
# count(子字符串.开始下标.结束下标)
# name = "tanhaitian1111"
# print(name.count("a",0,4))              在0.4中a的值只有一次出现，返回1
# print(name.count("a",20,21))           返回0：未包含

# 字符串判断
# name = "tanhaitian1111"
# print(name.endswith("1"))      返回True，结论为真，意思是该字符串以1结尾为真
        # endswith是否以某字符结束ian2211，修改次数为两次

# split() 指定分割符切割字符
#capitalizee()第一个小字符转成大写，其余字符转成小写
# print(name.capitalize())
# name = "tanhaitian1111"
# print(name.split("1",
# # # print(name.endswith("1"))        返回false，结论为假，意思是该字符串以1结尾为假
# #         # startswith是否以某字符开头
# #
# # # 字符串修改
# # # replace()替换
# # # name = "tanhaitian1111"
# # # print(name.replace("1","2"))    返回tanhaitian2222
# # # print(name.replace("1","2",2))     返回tanhait3))    返回['tanhaitian', '', '', '1']，将1替换成，完成分割

# 列表
# 列表名 = [元素1，元素2，元素3.]
# 所有元素放在[]内，元素与元素之间用，隔开
# 元素之间的数据类型各不相同
# 假设有一个列表名为li的列表内有元素1,2,3,4,'a'
# li = [1,2,3,4,'a']
# print(li[0],li[1])  返回1,2