t=int(input())
l1=[1,2]
l2=[1,3]
l3=[2,3]
l=l1
f=0
for test in range(t):
    p=int(input())
    if p==l[0]:
        if l==l1:
            l=l2
        elif l==l2:
            l=l1
        elif l==l3:
            l=l1
    elif p==l[1]:
        if l==l1:
            l=l3
        elif l==l2:
            l=l3
        elif l==l3:
            l=l2
    else:
        f=1
        print("NO")
        break
        
if f==0:
    print("YES")
            
