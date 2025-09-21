size = int(input("Enter the size of the pattern: "))
init = 0
while init < size:
    for nums in range(1, size+1):
        print("*", end='')
    print()
    init+=1