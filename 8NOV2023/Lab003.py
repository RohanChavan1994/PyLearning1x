class Password:
    def __init__(self, pwd):
        self.__password = pwd

    def password_len(self):
        print("Length of password:", len(self.__password))

    def set_new_password(self, pwd):
        if len(pwd) > 8:
            self.__password = pwd
        else:
            print("Weak password")

    def get_password(self, is_verified):
        if is_verified:
            return self.__password
        else:
            return "User not verified"


password1 = Password("Cronus123")
print(password1.get_password(True))
password1.password_len()

password1.set_new_password("Olympus888")
print(password1.get_password(True))
password1.password_len()

password1.set_new_password("888")
print(password1.get_password(True))
password1.password_len()

password1.set_new_password("LottoLand111")
print(password1.get_password(False))
password1.password_len()
