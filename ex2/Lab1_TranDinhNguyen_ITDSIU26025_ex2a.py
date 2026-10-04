number = int(input("Enter number : "))

if number < 1 or number > 10:
        print( "error",number, "is out of range [1, 10]")
else:
        print("Square of", number, "is", number ** 2)
