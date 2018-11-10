s=input()
l=list(s)
a=[]
for i in range(len(l)-1,-1,-1):
    a.append(l[i])
p="".join(l)
q="".join(a)
if p==q:
    print("YES")
else:
    print("NO")
