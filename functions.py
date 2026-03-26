# def my_func():
#     print("Hello pyhton")

# my_func()


# def my_func(a, b):
#     print(f"b: {b}, a: {a}")
#     res = a + b
#     #print(res)
#      return res

# #my_func(b=12, a=10)
# print(my_func(b=12, a=10) + 20)


def my_func():
    return

print(my_func)

def my_func(a, b):
    res = f"{a + b}"
    return res

ans= my_func(b=12, a=10)
print(type(ans))


#Default value should be at the end

def my_func(b, c, a=10):
    res = f"{a + b}"
    print(c)
    return res

ans= my_func(b=12, c={"a": 125, "b": 250})
print(ans)

