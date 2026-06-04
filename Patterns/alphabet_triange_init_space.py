for r in range(65,70):
    for c in range(65,70):
        if c>=r:
            print(chr(c),end=" ")
        else:
            print(" ",end=" ")
    print()