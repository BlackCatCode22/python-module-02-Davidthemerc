firstInteger = int(input("Enter the first integer: "))
secondInteger = int(input("Enter the second integer: "))
thirdInteger = int(input("Enter the third integer: "))

if firstInteger>secondInteger:

    if firstInteger>thirdInteger:
        print("Largest Integer (First): " + str(firstInteger))
    else:
        print("Largest Integer (Third): " + str(thirdInteger))
else:
    if secondInteger>thirdInteger:
        print("Largest Integer (Second): " + str(secondInteger))
    else:
        print("Largest Integer (Third): " + str(thirdInteger))