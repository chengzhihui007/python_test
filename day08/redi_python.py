#pip install redis
import redis

#1.连接数据库 key-value
client = redis.StrictRedis(host='192.168.124.132',port=6379)

#2,设置key
key = 'pyone'
#3,string 增加
client.incr('aaa')
result = client.set(key,"1")
#4.删 成功1 失败0
result = client.delete(key)
print(result)
#5.改
#result  = client.set(key,"2")

#6.查询 - bytes
result = client.get(key)

#查看所有的建
result = client.keys('*')
print(result)