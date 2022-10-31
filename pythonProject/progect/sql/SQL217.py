import pymysql;

def 创建表():
    db_config={"host":"60.205.224.199",
               "user":"root",
               "password":"aHX87EbGGC5rX2FE",
               "database":"test",
               "port":"3306"}

    con = pymysql.connect(db_config)# 创建链接对象
    cur = con.cursor()# 创建游标对象

    # 编写mysql

    sql ="""
        create table student(
        suo int primary key auto_increment,
        sname varchar(30)not null,
        age int(2),
        score float(3,1))
        """
    try:
        cur.execute(sql)# 执行SQL
        print("创建表成功")
    except Exception as e:
        print(e)
        print("创建表失败")
    finally:
        con.close()# 关闭连接

创建表()
