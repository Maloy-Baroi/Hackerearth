def func(l,r,k):
    count=0
    if k>r or l==r:
        return 0
    elif k>(r//2):
        return 1
    elif l<k and k<(r//2):
        count=1
        for i in range(k*2,r,1):
            if i%k==0:
                count+=1
        return count
    else:
        for i in range(l,r+1,1):
            if i%k==0:
                count+=1
    return count


x,y,z=map(int,input().split())
print(func(x,y,z))
