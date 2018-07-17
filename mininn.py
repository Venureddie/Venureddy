l= []
v = int(input())
lst = map(int,input().strip().split())
l.append(lst)
l.sort()
print(min(lst))
