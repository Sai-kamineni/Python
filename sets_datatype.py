#Set doent allow duplicates, there is no order in output
#we cant change the values once we define

s = {'a', 'a', 'b', 'c'}  
print(s)    #{'a', 'c', 'b'}

#print(dir(s))
#'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update



thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)    #{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)        #{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

banana
cherry
apple