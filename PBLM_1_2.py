# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
p=n*2-1
l=[n for i in range(n*2-1)]
print(' '.join(map(str,l)))
for i in range(1,n):
    for j in range(i,p-i):
        l[j]=l[j]-1
    print(' '.join(map(str,l)))
    
for i in range(n-1):
    for j in range(n-1-i,n+i):
        l[j]+=1
    print(' '.join(map(str,l)))
        
