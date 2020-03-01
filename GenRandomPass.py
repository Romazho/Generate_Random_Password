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


def genRandomCustomPassword():
    totalCustomLength = 0

    while(True):
        lengthOfPass = verifyIfInt("What is the length of your password: ")

        numOfUpperCaseLetters = verifyIfInt(
            "How many UPPER case letters would you like? ")
        numOfLowerCaseLetters = verifyIfInt(
            "How many lower case letters would you like? ")
        numOfNumbers = verifyIfInt("How many numbers would you like? ")

        totalCustomLength += numOfUpperCaseLetters + \
            numOfLowerCaseLetters + numOfNumbers

        if(totalCustomLength > lengthOfPass):
            print("The total length of you custum pass (" + str(totalCustomLength) +
                  ") is longer than: " + str(lengthOfPass) + ". Try again.")
        else:
            break

    password = genRandomPassword(lengthOfPass)
    while(sum(c.isupper() for c in password) < numOfUpperCaseLetters or
            sum(c.islower() for c in password) < numOfLowerCaseLetters or
            sum(c.isdigit() for c in password) < numOfNumbers):
        # print(password) #uncomment to debug
        password = genRandomPassword(lengthOfPass)

    return password


def verifyClientInput(stringToPrint):

    clientAnswer = input(stringToPrint).upper()
    while (clientAnswer != "N" and clientAnswer != "Y"):
        print("Invalid input!")
        clientAnswer = input(stringToPrint).upper()
        print(clientAnswer)

    return clientAnswer


def generatePassword():

    isPassFullyCustom = verifyClientInput(
        "Would you like to fully customize your password? n/y: ")

    if(isPassFullyCustom == "N"):
        clientRange = verifyMinMax()
        lengthOfPass = random.randint(clientRange[0], clientRange[1])
        passWord = genRandomPassword(lengthOfPass)
        print("The length of your password is: " + str(lengthOfPass))
    else:
        passWord = genRandomCustomPassword()

    print("Password: " + passWord)


generatePassword()
