n=int(input())
if n==1:
    print(n)
for num in range(2,n,1):
    if num==2 or num==3:
        print(num, end=" ")

    if num > 3 and num%2!=0:
       for i in range(3,num):
           if (num % i) == 0:
               break
       else:
           print(num,end=" ")
           
