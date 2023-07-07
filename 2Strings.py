# string is immutable

course = "Python Programming"

print(len(course))
print(course[0])
print(course[1])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])


print(id(course))
print(id(course[0]))


# formatted strings
first = "Archana"
second = "sana"
x = first +" " +second
print(x)

#using formatted string 
y = f"{first} {second}"
print(y)

z = f"{ 2 + 2 } {second}"
print(z)