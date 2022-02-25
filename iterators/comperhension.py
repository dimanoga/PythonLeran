lst =[1,2,3,4,5,6,-1]
z = [x * x for x in lst if x % 3]
print(z)





z = [(x,y) for x in range(3) for y in range(3) if y>=x]
print(z)
z=[]
for x in range(3):
    for y in range(3):
        if y>=x:
            z.append((x,y))
print(z)


z = ((x,y) for x in range(3) for y in range(3) if y>=x)
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))