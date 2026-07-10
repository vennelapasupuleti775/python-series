num=int(input("enter the number:"))
for i in range(1,n+1):
    if num%i==0:
         count+=1
    if count==2:
         print("prime")
    else:
         print("not prime")
