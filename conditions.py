# if, elseif, else

num1 = 500

if num1 <= 100:
    print("number is lessthan or equal to 100")
else:
    print("number is greater than 100")

if (num1 <= 100) and (num1 >= 50):
    print("number is lessthan or equal to 100")
else:
    print("number is greater than 100")


# num1 = 500

# if (num1 > 50) and (num1 <= 100):
#     print("Number is less than or equal to 100 and greater than 50")
# elif num1 <= 50:      # elif: else if
#     print("Number is less than or equal to 50")
# else:
#     print("Number is greater than 100")

if True:
    print("Iam evaludated")

# Anything that is non-zero is considered as true
if "false":
    print("I am evaluated")
else:
    print("Zero")