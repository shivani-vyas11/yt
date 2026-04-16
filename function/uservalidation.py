def login_system():
    attempts = 3

    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == "admin" and password == "admin123":
            return "Login Successful"
        else:
            attempts -= 1
            print("Incorrect credentials. Attempts left:", attempts)

    return "Account Locked"

print(login_system())