x=("apple","banana","kiwi","tomato")
y=list(x)
#y[1]="kiwi"
#x=tuple(y)
#print(x)
#print(len(x))
#a=("banana",)
#print(type(a))
#y.append("orange")
#x=tuple(y)
#print(x)
y.remove("kiwi")
x=tuple(y)
#print(x)
#str="".join(x)
#print(str)
a=("1","2","3","4","5","6")
print(a)
y=a[5]
print(y)
c=("1","1","4","4","6","8")
count=c.count("4")
print(count)
a=c[:3]+c[5:]
print(a)
#unzip the list of tuples
s=[(2,3),(4,6),(6,7)]
print(list(zip(*s)))
x=("sreehari")
y=reversed(x)
print(tuple(y))