with open(r"D:\1.jpg","rb") as  r:  #读取第一个文件
    with open(r"D:\2.jpg","wb") as w: #指定写入路径
        for aa in r.readlines(): #对第一个文件进行读取遍历
            w.write(aa) #将第一个遍历出来的内容写入到指定的文件路径对象
print("复制成功")