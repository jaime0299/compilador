ban=0

for i in range(10):
    print(i)
    if i==5 and ban==0:
        i=2
        ban=1
        print("Entra")