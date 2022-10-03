x=int(input(f"x="))
y=int(input(f"y="))
z=int(input(f"z="))
p=int(input(f"p="))
for x in range (p-1):
	for y in range (p-1):
		z=(x*y//p)=10+(x*y)%p
print(z)