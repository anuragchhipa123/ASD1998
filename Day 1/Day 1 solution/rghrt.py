n=int(input("enter a no."))
s=0
while n:
    s=s+n%10
    n=n//10
    print(s)
    
