import pymysql

con = pymysql.connect(host="60.205.224.199", user="root", password="pass", database="test", port=3306)# 创建链接对象
print(con)
sun=con.cursor()# 创建游标对象

sql='insert into student (sname,age,score) values("张三",25,99.8),("李四",19,95.9),("王二",25,35.5)'
try:
    sun.execute (sql)# 执行SQL
    con.commit()# 提交事务
    print("插入成功")

except Exception as  e:
    print(e)
    con.rollback()# 回滚事务
    print("插入失败")
finally:
    sun.close()