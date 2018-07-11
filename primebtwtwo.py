a,b=map(int,raw_input().strip().split())
for num in range(a+1,b):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
