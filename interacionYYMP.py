def fiboiter(n):
    global cnt
    fib=[1,1]
    for k in range(2,n+1):
        cnt+=1
        fib.append(fib[k-1]+fib[k-2])
    return fib[n]

for n in range(0,101):
    cnt=0
    a=fiboiter(n)
    cntr,cnt=cnt,0
    print(n,fiboiter(n))
