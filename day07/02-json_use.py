import json

#1. 字符串和dict list转换

#字符串(json)----dict list
data = '[{"name":"张三","age":20},{"name":"李四","age":18}]'
list_data = json.loads(data)
print(type(list_data))
# dict list ---字符串
list2 = [{"name":"张三","age":20},{"name":"李四","age":18}]
data_json = json.dumps(list2)
print(type(data_json))

# 2. 文件对象 和 dict  list 转换

# dict list 写入文件

# with open ('02json.json', 'w') as f:
#     f.write(data_json)

# ftp 是file path
fp = open('02new.json', 'w')
json.dump(list2,fp)
fp.close()

#读取文件 -- list dict
result = json.load(open('02new.json','r'))
print(result)