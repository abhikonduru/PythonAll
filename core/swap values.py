#abhi way
a=10
b=30
swap1 = b-a
swap2 = a-b
a=a+swap1
b=b+swap2
print(a)
print(b)

#smart way
a=10
b=30
#c=0 dont need c=0 bc you are saying c=b in the next line
c=b
b=a
a=c
print(a)
print(b)

#no temporary variable
a=10
b=30
a=a+b
b=a-b
a=a-b
print(a)
print(b)