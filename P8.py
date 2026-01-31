# Exception Handling Program with Reasons


# SyntaxError
try:
    eval("if True print('Hello')")
except SyntaxError as e:
    print("SyntaxError Reason:", e)
    
# ZeroDivisionError
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError as e:
    print("ZeroDivisionError Reason:", e)

# ValueError
try:
    num = int("abc")
except ValueError as e:
    print("ValueError Reason:", e)

# NameError
try:
    print(x)
except NameError as e:
    print("NameError Reason:", e)

# IndexError
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError as e:
    print("IndexError Reason:", e)


print("Abhay Yadav F123")


