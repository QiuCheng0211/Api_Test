#使用pickle实现序列化和反序列化_神经元记忆和移植
import pickle

a1='珊珊'
a2=123
a3=[10,20,30]
print(id(a1))
print(id(a2))
print(id(a3))

with open(r"D:\text124.txt","wb") as f:
    pickle.dump(a1,f)
    pickle.dump(a2,f)
    pickle.dump(a3,f)

with open(r"D:\text124.txt","rb") as f:
    b1=pickle.load(f)
    b11=pickle.load(f)
    b10=pickle.load(f)

print(id(b1)),print(id(b11)),print(id(b10))
print(b1),print(b11),print(b10)
