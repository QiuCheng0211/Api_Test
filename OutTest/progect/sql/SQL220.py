import pymysql

A = pymysql.connect(host="60.205.224.199", user="root", password="pass", database="test", port=3306)# 创建链接对象
print(A)
B=A.cursor()#创建游标

sql="update student set age=18 where age=19"  #更新语句SQL
sql2="delete from student where score=35.5"  #删除SQL语句

try:
    B.execute(sql)#执行sql
    A.commit()#提交事务
    print("更新成功")
except BaseException as e:
    print(e)
    A.rollback()#回滚事务
    print("更新失败")
finally:
    A.close()