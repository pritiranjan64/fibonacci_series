#wap to print first N fibonacci series.
n=int(input())
f=int(input('enter first values of fibonacci series:'))
s=int(input('enter second values of fibonacci series:'))
if n==1:
    print(f)
else:
    print(f,s,end=' ')
    for i in range(n-2):
        t=f+s
        print(t,end=' ')
        f,s=s,t      


#wap to print Nth number fibonacci series.
n=int(input())
f=int(input('enter first values of fibonacci series:'))
s=int(input('enter second values of fibonacci series:'))
if n==1:
    print(f)
elif n==2:
    print(s)
else:
    for i in range(n-2):
        t=f+s
        f,s=s,t
    print(t)    