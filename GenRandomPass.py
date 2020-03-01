import random
import string
import secrets


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

    return int(valToVerify)


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


def genRandomPassword(lengthOfPass):
    passWord = ""
    randomInt = random.randint(0, 2)
    for i in range(lengthOfPass):
        if(randomInt == 0):
            passWord += secrets.choice(string.digits)
            randomInt = random.randint(0, 2)
        elif(randomInt == 1):
            passWord += secrets.choice(string.ascii_letters)
            randomInt = random.randint(0, 2)
        else:
            passWord += secrets.choice(string.punctuation)
            randomInt = random.randint(0, 2)

    return passWord


def genRandomCustomPassword(lengthOfPass):
    # numOfLetters = input("How many letters would you like?")
    # numOfUpperCaseLetters = input(
    #     "How many UPPER case letters would you like?")
    # numOfLowerCaseLetters = input(
    #     "How many lower case letters would you like?")
    # numOfNumbers = input("How many numbers would you like?")
    pass


def verifyClientInput(stringToPrint):

    clientAnswer = input(stringToPrint).upper()
    while (clientAnswer != "N" and clientAnswer != "Y"):
        print("Invalid input!")
        clientAnswer = input(stringToPrint).upper()
        print(clientAnswer)

    return clientAnswer


def generatePassword(min, max):
    lengthOfPass = random.randint(min, max)

    isPassFullyCustom = verifyClientInput(
        "Would you like to fully customize your password? n/y: ")

    if(isPassFullyCustom == "N"):
        passWord = genRandomPassword(lengthOfPass)
    else:
        passWord = genRandomCustomPassword(lengthOfPass)

    print("The length of your password is: " + str(lengthOfPass))
    print("Password: " + passWord)


def main():
    # characters = string.ascii_letters + string.digits  # + string.punctuation

    clientRange = verifyMinMax()
    generatePassword(clientRange[0], clientRange[1])


main()
