def is_palidrome(x):
    if x < 0:
        return false
    return str(x)==str(x)[::-1]

x = int(input("enter an integer:"))
result=is_palidrome(x)
if result:
    print("the integer is a palindrome.")
else:
    print("the integer is not a palidrome.")
