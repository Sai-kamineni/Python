#For , for-else, while, while-else
#continue, break

l= [10, 20, 30, 40, "abcd", False]

#for num in l:
#    print(num)

for num in l:
    if type(num) == str:
        print(num)

#Find the first string element inside the gien list
l= [10, 20, 30, 40, "abcd", False, "abcde"]

for num in l:
    if type(num) == str:
        print(num)
        break

#Find elements that are integer and add 10 to them insde the given list

for num in l:
    if type(num) == int:
        print(num + 10)
        continue
    print("Iam outside if block")
else:
    print("Iam outside for loop and loop got exited without any break statment")


#while

idx = 0

while idx < len(l):
    ele = l[idx]
    if type(ele) == int:
        print(ele + 10)
        # idx = idx + 1
        idx += 1
        continue
    if type(ele) == str:
        print(ele)
        break
    print("I am outside if block")
    idx += 1
else:
    print("I am outside loop and loop got exited without any break statement")


# d = {'k': 123, (1, 2, 3, 4): 123, (1, 2, 3, 4, 5): list(str(123))}
# for k, v in d.items():
#     print(k, v)


l = (10, 20, 30, "abcd", False, "abcde")
# for idx, ele in enumerate(l):
#     print(idx, ele)

print(list(range(len(l))))

for idx in range(len(l)):
    print(l[idx])