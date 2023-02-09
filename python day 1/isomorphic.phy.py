def sumsquare(l):
    odd=0
    even=0
    for num in l:
        if num%2==0:
            even+=num*num
        else:
            odd+=num*num
    return[odd,even]

l=list(map(int,input("Enter a list of intrgers sepertaed by space:").strip().strip().split()))
result = sumsquare(l)
print("the sum of squars of odd numbers is:",result[0])
print("the sum of sqares of even numbers is:",result[1])
