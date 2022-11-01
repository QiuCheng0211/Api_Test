import pymysql

con = pymysql.connect(host="60.205.224.199", user="root", password="pass", database="test", port=3306)# 创建链接对象
print(con)
sun=con.cursor()# 创建游标对象

sql='select * from student'
try:
    sun.execute(sql)# 执行SQL
    students=sun.fetchall()#处理结果集
    print(students)
    for student in students:
        print(student)
        sno = student[0]
        sname = student[1]
        age = student[2]
        score = student[3]
        print("编号:", sno, "s姓名:", sname, "年龄:", age, "成绩:", score, )
except Exception as e:
    print(e)
    print("查询失败")
finally:
    sun.close()