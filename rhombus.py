#ask a user for integer representing the number of rows
#if odd generate a rhombus of asterisks with as many rows as the user wants,
#otherwise ask the user to input the value again

r = int(input("Enter a number of rows: "))
empty = " "

if r % 2 != 0:
    #generate rhombus of asterisks with rows r
    #print spaces
    for i in range(int((r/2)+1)):
        space = (empty * (int((r/2)+1)-i))
        star = ("* " * i)
        print(space + star)

    print( "* " * (int(r/2) + 1))

    for i in range(int((r/2)),0,-1):
        space = (empty * (int((r/2)+1)-i))
        star = ("* " * i)
        print(space + star)

    
    print()
else:
    print("Please input a difference number of rows: ")
