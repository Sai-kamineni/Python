#List

#List is a collection of values
#Nested list ex below

""" l = [1, 2, 3 ,"abc", True, [10, 20, 40 ,"abc"]]
print(l)   
#[1, 2, 3, 'abc', True, [10, 20, 40, 'abc']]

l1 = l[3]  
print(l1)   #abc

l2 = l[5][0]   
print(l2)    #10

l2 = l[-1][0]
print(l2)    #10

print(len(l) - 1)  #5

print(dir(l))
 """
#'append', 'clear', 'copy', 'count', 'extend', 'index', 
# 'insert', 'pop', 'remove', 'reverse', 'sort'


l = [1, 2, 3 ,"abc", False]

#append an element to the end of the list
l.append(True)
print(l)      #[1, 2, 3, 'abc', False, True]

l.append([3, 2, 1, 'abc', False, True])
print(l)      # [1, 2, 3, 'abc', False, True, [3, 2, 1, 'abc', False, True]]

#Inplace operation
l.insert(0, "abc")  
print(l)           #['abc', 1, 2, 3, 'abc', False, True, [3, 2, 1, 'abc', False, True]]

res=l.insert(0, "abc")
print(res, 1)       #None 1

#l = [3, 2, 1, 'abc', False, True]
l.extend([1,2,3, "mba"])
print(l)     #[3, 2, 1, 'abc', False, True, 1, 2, 3, 'mba']

#Inplace operation
l = [2, 3, 1]  
l.sort()
print(l)

#I dont want inplace operaion , sorted returns a new list.
l1=sorted(l) 
print(l, l1)   #[2, 3, 1] [1, 2, 3]

#List is a mutable datatype (we can change the values in list)
