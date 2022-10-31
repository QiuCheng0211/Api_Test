with open(r"D:\text120.txt","r",encoding="utf-8") as a:
    lines=a.readlines()
    lines=[line.rstrip()+"#"+str(index+1)+"\n" for index,line in enumerate(lines)]  #遍历出来 并且替换lines内容

with open(r"D:\text120.txt","w",encoding="utf-8") as f:
    f.writelines(lines)#写入