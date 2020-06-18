# Maximum and minimum number from console
# Traditional looping techniques
# Exits when user enters "done"
# in-built functions min() and max() are one line subsitutes
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    else:
        flag=False
        try:
            n=int(num)
            flag=True
        except:
            print("Invalid input")
        if flag:
            if largest is None:
                largest=n
            elif n>largest:
                largest=n
            if smallest is None:
                smallest = n
            elif n<smallest:
                smallest=n
print("Maximum is", largest)
print("Minimum is", smallest)
