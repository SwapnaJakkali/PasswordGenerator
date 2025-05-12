import secrets

def passwordgen(length,lowercase,uppercase,symbols,numbers):
    allowedchars = lowercase + uppercase + symbols + numbers
    password = ""

    for i in range(length):
        randindex=secrets.randbelow(len(allowedchars))
        password+=allowedchars[randindex]
    print(password)
length = 10
lowercase = "abcdefghijklmnopqrstvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*"
numbers = "123456789"
passwordgen(length , lowercase , uppercase , symbols , numbers)

