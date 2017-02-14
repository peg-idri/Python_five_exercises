#coding:utf-8
# 题 1
# 检查密码规则合法性
# 考察基本编码能力和字符串处理
# 参考 python 文档的字符串库
# 给定一个字符串，用以下规则检查合法性
# 完全符合返回 True，否则返回 False
# 1，第一位是字母
# 2，只能包含字母、数字、下划线
# 3，只能字母或数字结尾
# 4，最小长度2
# 5，最大长度10

# Hello World program in Python

import string

def valid_password(pwd):
	s = pwd

	#1
	con1 = s[0] in string.ascii_letters
	print con1
	#2		
	con2 = True
	for i in s:
		if i not in string.ascii_letters+'_'+string.digits:
		    con2 == False
	print con2
	#3
	con3 =  s[-1]  in string.ascii_letters + string.digits
	print con3
	#4、5
	con45 = (len(s) >= 2 and len(s) <= 10)
	print con45
	
	if con1 and con2 and con3 and con45:
		print "pwd is valid"
	else:
		print "pwd is invalid"
	
pwd = 'w'
valid_password(pwd)	


# 题 2
# 返回 100 内的素数列表
# 考察基本的循环和选择概念、列表的使用

def prime_numbers():
    li = []
    for su in range(2,100):
        i = 2
        is_prime = True
        while i*i <= su:
            if su%i == 0:
                is_prime = False
            i += 1
        if is_prime:
            li.append(su)
    print li

def prime_numbers():
    l2 = []
    for x in range(2,100):
        n = 0
        for y in range(1,x+1):
            if x % y == 0:
                n = n+1
        if n==2:
            l2.append(x)
    print l2

# 题 3
# 给定一个只包含字母的字符串，返回单个字母出现的次数
# 考察字典的概念和使用
# 返回值为包含元组的列表，格式如下（对列表中元组的顺序不做要求）
# 参数 "hello"
# 返回值 [('h', 1), ('e', 1), ('l', 2), ('o', 1)]

def letter_count(str):
    dict1 = {}
    for i in str:
        if i not in dict1:

            dict1[i] = 1
        else:
            dict1[i] += 1

    print dict1
str = 'hello'
letter_count(str)


# 题 4
# 给定一个英文句子（一个只有字母的字符串），将句中所有单词变为有且只有首字母大写的形式

# string.split(str='', num=string.count(str))
#string.join(sep)

def cap_string(str):
    strs = str.split(" ")
    for i in range(len(strs)):
        strs[i] = strs[i].capitalize()
    return " ".join(strs)

print cap_string("hey hey he2")



# 题 5
# 写一个 Queue 类，它有两个方法，用法如下

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue()) # 1
print(q.dequeue()) # 2
print(q.dequeue()) # 3