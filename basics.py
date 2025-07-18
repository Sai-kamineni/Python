#Integer

""" res = 10 + 20
print(res) #print ("Result: ", res)

print(id(res)) #print ("Mem add: ", id(res))

#There are mrthods specific to that data type
print(type(res))  #print("Data type:", type(res))
 """

#Float

""" a = 10.23
b = 20.34
res = a + b
print("Result:", res, "Type:", type(res))

#Result: 30.57 Type: <class 'float'> """


#String

""" sample_str = "this is a string"

print(sample_str, type(sample_str))
#o/p:this is a string <class 'str'>

print(dir(sample_str))

"""  'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 
'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 
'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 
'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 
'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill' """

print(sample_str.capitalize())    #This is a string

sample_str = "This is a String"

print(sample_str.casefold())  #this is a string

print(sample_str.swapcase())   #tHIS IS A sTRING

print(sample_str.split(' '))   #['This', 'is', 'a', 'String']

#In python index starts from 0
print(sample_str.index('T'))   #0 
print(sample_str.index('g'))   #15

sample_char = sample_str[-1]
print(sample_char)               #g

print(len(sample_str))     #16 """


#Boolean
""" 
a = True
b = False

print(a and b)  #False
print(a or b) #True

a = 2
b = 4

print(a + b)  #6  
print(a - b)  #-2
print(a * b)  #8
print(a / b)  #0.5
print(b % a)  #0
print(a // b) #0
print(a ** b) #16
 """