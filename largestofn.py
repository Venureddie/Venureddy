a=[]
n=int(raw_input())
for i in range(1,n+1):
    b=int(raw_input())
    a.append(b)
a.sort()
print(a[n-1])
