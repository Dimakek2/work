sob = [20,2,5,0,10,5]
count = 0
x=0
for i in range(len(sob)-1):
    for i in range(len(sob) - 1):
        if sob[i]>sob[i+1]:
            count = sob[i]
            sob[i] = sob[i+1]
            sob[i+1] = count
            x+=1
print(x)
print (sob)


