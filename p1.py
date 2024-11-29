l=[1,1,2,2,3,4,1,3]
n,i=len(l),0
while i<n:
    if l.count(l[i])>1:
        l.pop(i)
        n-=1
    i+=1
print(l)
