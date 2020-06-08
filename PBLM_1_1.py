t=int(input())

for test in range(t):
    p=int(input())
    c=0
    c+=int(p/100)
    p=p%100
    c+=int(p/20)
    p=p%20
    c+=int(p/10)
    p=p%10
    c+=int(p/5)
    p=p%5
    c+=int(p)
    print(c)
    
    
