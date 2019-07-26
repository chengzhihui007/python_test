# 安装 pymongo pip install pymongo
import pymongo

try:
    # 1.连接数据库
    mongo_py = pymongo.MongoClient()

    # 2. 库和表的名字； 有数据会自动建库建表
    # 2.1数据库
    db = mongo_py['six']
    # 2.2 表 集合
    collection = mongo_py['six']['stu']

    # 3.插入数据
    one = {'name': '张三', 'age': 50}
    two_many = [
        {'name': '小三', 'age': 30},
        {'name': '李四', 'age': 40},
        {'name': '王五', 'age': 50},
        {'name': '赵六', 'age': 60},
        {'name': '小七', 'age': 17},
        {'name': '老八', 'age': 80}
    ]
    #collection.insert_one(one)
    #collection.insert_many(two_many)
    #collection.insert()

    #删除数据
    # collection.delete_one({"age": 15})
    # collection.delete_many({"age": 15})

    #修改数据
    #collection.update({"age":17},{"$set":{"age":7}})

    #查询
    result = collection.find({"age":7})
    for i in result:
        print(i)
except Exception as e:
    print(e)
# 4.关闭数据库
mongo_py.close()
