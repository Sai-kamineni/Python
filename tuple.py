t = (1, 3, 5, "true", [10,30,50])
# print(t, type(t))   #(1, 3, 5, 'true', [10, 30, 50]) <class 'tuple'>

# t1 = t[-1]
# print(t1)   #[10, 30, 50]

#Tuple is an immutable datatype
#t[0] = 100    #TypeError: 'tuple' object does not support item assignment
#print(t)

#print(dir(t))
#'count', 'index'

print(t.index("true"))   #3

t = (1, 2, 3, 1)
print(t.count(1))    #2

#Unpacking
t = (1, 2)
t1, t2 = t
print(t1, t2)    #1 2
