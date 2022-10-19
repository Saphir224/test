import operator as op
firstnum = float(input("Enter the first number: "))
secondnum = float(input("Enter the second number: "))
if secondnum !=0:
    print("The numgber entered is: " + str(firstnum) + " and " +  str(secondnum))
else:
    print("You must be enter the second number different to zero")
opera = input("Enter operator that you want between those --> (+,-,*,/):")
if opera == "+":
    somNum= op.add(firstnum, secondnum)
    print("the somme of numbers is: "+ str(somNum) )
elif opera == "-":
    print("the differce is " + str(op.sub(firstnum, secondnum)))
elif opera== "*":
    print("The multiplcation is: "+ str(op.mul(firstnum, secondnum)))
elif opera == "/":
    print("The division is: " + str(op.truediv(firstnum, secondnum)))
else:
    ("The operator is not good, you must add a operator between those (+,-,*,/)")