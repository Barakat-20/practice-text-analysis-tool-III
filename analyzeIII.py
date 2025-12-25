from random_username.generate import generate_username
# welcome user
def welcomeUser():
    print("\nWelcome to the text analysis tool")

#Get Username
def getUsername():
    #Print message prompting user to enter username and get user input
    print("\nTo begin, please enter your username:")
    usernameFromInput = input("\n")

    usenameLessThan5Chars = len(usernameFromInput) < 5
    isValidIdentifier = not usernameFromInput.isidentifier()

    #usernameContainsSpaces = " " in usernameFromInput
    #print("Your username contain spaces: " + str(usernameContainsSpaces))
    #firstCharIsNumber = usernameFromInput[0].isdigit()
    #print("Your first chracter is digit: " + str(firstCharIsNumber))

    usernameIsInvalid = usenameLessThan5Chars or isValidIdentifier #(usernameContainsSpaces or firstCharIsNumber)

    if usernameIsInvalid:
        print("\nYour username must be at least 5 characters long, alphanumeric only, have no spaces, and cannot start with a number")
        print("\nAssigning new username... ")
        usernameFromInput = generate_username()[0]

    return usernameFromInput

# Greet user
def greetUser(name):
    print("Hello, " + name)
    
welcomeUser()
username = getUsername() 
greetUser(username) 

# a function can accept as many parameters as it need, you just need to define them by separating them with comma
# parameter function. you must also call a function with the number of parameters. in js it will just mark it as undefined. make sure what you are concatinating is of the same data type