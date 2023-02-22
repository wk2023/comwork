'''
a =[1,2,3,4]
print(type(a))
#print(dir(a))
a_inter = iter(a)
print(a_inter)
print(dir(a_inter))
print(a_inter.__iter__)
print(next(a_inter))
'''
b = [x for x in range(1,9)]
print(type(b))
print(b)
c = (x for x in range(1,9))
print(type(c))
print(c)
print(dir(c))