def fibg():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
        
def fib(n):
    res = [0,1]
    for i in range (2,n+1):
        tmp = res[i-1] + res[i-2]
        res.append(tmp)
    print res
    return res[n]

f=fib(9)
print f


max=9
giter=fibg()
count=0
for i in giter:
    print i
    count+=1
    if (count>max):break
