#Dictionary is a key value pair
#A dictionary is a mutable datatype

d = {'k': 123}
print(d['k'])   #123

d = {'k': 123, 'k': 1234}  #replaces the old value
print(d['k'])   #1234

d = {'k': 123, (1, 2, 3, 4): list(str(123))} 
print(d[(1, 2, 3, 4)])    #['1', '2', '3']


#print(dir(d))
#clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values

print(d.keys())    #dict_keys(['k', (1, 2, 3, 4)])
print(d.values())  #dict_values([123, ['1', '2', '3']])
print(d.items())    #dict_items([('k', 123), ((1, 2, 3, 4), ['1', '2', '3'])])

#Can replace the value
d['k'] = 1234
print(d)    #{'k': 1234, (1, 2, 3, 4): ['1', '2', '3']}