import pymysql

def 更新删除():
    A = pymysql.connect(host="60.205.224.199",user="root", password="aHX87EbGGC5rX2FE", database="test", port=3306)# 创建链接对象
    print(A)
    B=A.cursor()#创建游标

    sql="update student set age=88 where age=18"  #更新语句SQL
    sql3="update student set sname=\"张振宇\" where sname=\"张三丰\""
    sql2="delete from student where score=35.5"  #删除SQL语句
    try:
        B.execute(sql3)#执行sql
        A.commit()#提交事务
        print("更新成功")
    except BaseException as e:
        print(e)
        A.rollback()#回滚事务
        print("更新失败")
    finally:
        A.close()

更新删除()