name  = "ada woNg"

print(name.title()) #--> outpt : Ada Wong


a = 5000
b = a
c = 5000

print( id(a) == id(b))
print( id(a) == id(c))
print( id(b) == id(c))
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))

print(id(a) is id(b))
print(id(a) is id(c))
print(id(b) is id(c))
id(a) is id(b)