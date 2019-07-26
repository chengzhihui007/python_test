# pip  install pymysql
import pymysql

try:
    # 1.连接数据库 连接对象 connection()
    conn = pymysql.Connect(
        host="localhost",
        port=3306,
        db='test',
        user='root',
        passwd='123456',
        charset='utf8'
    )
    # 2.创建游标对象 cursor()
    cur = conn.cursor()

    #增加一条数据 student
    #insert_sub = 'insert into student values(4,"啊大佬A" , 12)'
    #result = cur.execute(insert_sub)

    #修改
    # update_sub = 'update student set name="大傻X123" where id = 4'
    # result = cur.execute(update_sub)

    #删除
    # del_sub = 'delete from student where id=1'
    # result = cur.execute(del_sub)

    #查询
    query_sub = 'select * from student'
    cur.execute(query_sub)
    result = cur.fetchall()
    print(result)
    #提交事务
    conn.commit()
    #关闭游标
    cur.close()
    #关闭连接
    conn.close()
except Exception as e:
    print(e)
