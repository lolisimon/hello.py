doors = [False] * 100

print("The following doors are open: ")

for i in range(0, 100):
    for j in range(i, 100, i+1):
        if ((j+1) % (i+1) == 0):
            doors[j] = not doors[j]
    
    if(doors[i]):
        print(i+1)