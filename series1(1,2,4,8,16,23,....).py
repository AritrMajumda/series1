n=int(input("enter the number= "))
m=int(input("enter the number= "))
s=n
print(s)
s1=0
while s<=m:
    k=s
    while k>0:
        p=int(k%10)
        s1=s1+p
        k=int(k/10)
    s=s+s1
    if(s<=m):
        print(s)
    else:
        StopIteration
    s1=0


