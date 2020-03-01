import random
import string


def verifyIfInt(stringToPrint):
    isNotInt = True
    valToVerify = input(stringToPrint)
    while(isNotInt):
        try:
            val = int(valToVerify)
            isNotInt = False
        except ValueError:
            print("You entered a string, you should enter a number. Try again.")
            valToVerify = input(stringToPrint)

    return valToVerify


def verifyMinMax():
    minRequest = "What is your MINIMUM password length:"
    maxRequest = "What is your MAXIMUM password length:"

    minPassLength = verifyIfInt(minRequest)
    maxPassLength = verifyIfInt(maxRequest)

    while(minPassLength > maxPassLength):
        print("Error, the minimum is higher than the maximum, please choose again your min and max.")
        minPassLength = verifyIfInt(minRequest)
        maxPassLength = verifyIfInt(maxRequest)

    return [minPassLength, maxPassLength]


def generatePassword(min, max):
    print(min)
    print(max)


def main():
    clientRange = verifyMinMax()
    generatePassword(clientRange[0], clientRange[1])


main()
