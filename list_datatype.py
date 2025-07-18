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

