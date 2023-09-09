#1
#print(bin(123)[2:])

#4
'''
c=[]
for N in range(1,150):
    N=bin(N)[2:]
    def ws(N):
    
        if int(N)%3==0:
            R = str(N)+str(N[-1])+str(N[-2])+str(N[-3])                                                  
            R = int(R,2)
        else:
            a = int(N)%3
            a = bin(a)[2:]
            R = str(N) + str(a)
            R = int(R,2)
        return R
    b = ws(N)
    
    if b>151:
        c.append(b)
print(min(c))
'''
#5
'''
x = 1
y= 0
z=0
w=1
F = (x and not y) or (y * z) or not w
if F==0:
    print(x,y,z,w)
'''
#6
c=[]
for i in range (0,10):
    for x in range(0,1000):
        a = '1'+str(i)+'2157'+str(x)+'4'
        a=int(a)
        if a%2024==0 and a<=10**10:
            c.append(a)
            c.append(a//2024)
for i in range (0,10):
    a = '1'+str(i)+'2157'+'4'
    a=int(a)
    if a%2024==0 and a<=10**10:
            c.append(a)
            c.append(a//2024)
for i in range(0,len(c),2):
    print(c[i],c[i+1])

















    
