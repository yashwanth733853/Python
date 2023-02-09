def countstrings(n,start):
    if n==0:
        retun 1
    count=0
    for i in range (start,5):
        count+=countsrings(n-1,i)
    return count
def countvovelstrings(n):
    return countstrings(n,0)

n=int(input("enter a number:"))
print(countvowelstrings(n))
cxxxxxx

