class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def login(self, username, password):
        if self.username == username and self.__password == password:
            print("Login successful.")
        else:
            print("Invalid username or password.")

user1 = User("Krishiv", "pass123")

user1.login("Krishiv", "pass123")  
user1.login("Krishiv", "wrong123")  
