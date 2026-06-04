num=int(input("enter the number: "))
rev=0
while num>0:
    r=num%10
    rev=(rev*10)+r
    num=num//10
while rev>0:
    r=rev%10

    match (r):
        case 1:
            print("one",end=' ')
        case 2:
            print("two",end=' ')
        case 3:
            print("three",end=' ')
        case 4:
            print("four",end=' ')
        case 5:
            print("five",end=' ')
        case 6:
            print("six",end=' ')
        case 7:
            print("seven",end=' ')
        case 8:
            print("eight",end=' ')
        case 9:
            print("nine",end=' ')
        case 0:
            print("zero",end=' ')
            
    rev=rev//10
        


        