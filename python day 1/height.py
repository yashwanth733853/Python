def is_valid_number(s):
    try:
        float(s)
        return true
    except valueerror:
        return false

s=(input("enter a string:"))
if(s.isdigit()):
    if is_valid_number(s):
        print (s,"is a valid number")
    else:
        print(s,"is not a valid number")

else:
    print("value is incorrect")
