n = int(input("Ener a number : "))
print()


for i in range(1, n+1):
    for j in range(1, n - i + 1):
        print(" ", end="")  
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()


for i in range(n-1, 0, -1):
    for j in range(1, n - i + 1):
        print(" ", end="")
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()