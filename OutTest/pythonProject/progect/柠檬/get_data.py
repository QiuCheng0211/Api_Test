


#反射与应用
#全局变量
class GetData:
    Cookie="小瓶子"

print(GetData.Cookie)
setattr(GetData,"Cookie","符")#setattr 可以把类里面的属性值进行修改
print(hasattr(GetData,"Cookie"))#hasattr 判断Cookie是否有值
print(getattr(GetData,"Cookie"))#getattr获取属性值
delattr(GetData,"Cookie")#delattr 删除Cookie属性值
print(hasattr(GetData,"Cookie"))#hasattr 判断Cookie是否有值

class GetData_001:
    Cookie=None #存储cookie初始化none



