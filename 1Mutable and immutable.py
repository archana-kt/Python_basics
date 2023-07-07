from re import X


x = 1
print(id(x))

#different memory allocated for x 
# now x refers to this memory
x = x + 1
print(id(x))
print(x)

#list
y = [1,2,3]
print(id(y))
y.append(4)
print(y)
print(id(y))

# see it mutable but can't change memory. So for same value, it will
# hold same memory for memory management.