import re

#1.拆分字符串
one = 'asdsfsqshs'

#标准是s为拆分
pattern = re.compile('s')
result = pattern.split(one)
print(result)

#2.匹配中文
two = 'sadfa我sadfasf是asdfafd你asdfasdffsf爸sadfasdfsad爸'
#python中 匹配中文 [a-z] unicode的范围 * + ?
pattern = re.compile('[\u4e00-\u9fa5]+')
result = pattern.findall(two)
print(result)