import sqlite3
import secrets


with sqlite3.connect('DBclients.sql') as connection:
    cursor = connection.cursor()

    class User:
        def __init__(self):
            self.login = input("username>> ")
            self.password = input("password>> ")
            self.randomkey = secrets.token_hex(3).upper()

        def login_user(self):
            cursor.execute("SELECT UserLogin, Password FROM clients WHERE UserLogin = ? AND Password = ?", (self.login, self.password))
            if not cursor.fetchone():
                print("Not found.")
                return None
            else:
                return self.randomkey

    class Info:
        def __init__(self, login, password, randomkey):
            self.login = login
            self.password = password
            self.randomkey = randomkey
            self.key = input("input your secret key>> ")

        def check_info(self):
            if self.key == self.randomkey:
                cursor.execute("SELECT Salary, Raising FROM clients WHERE UserLogin = ?", (self.login,))
                result = cursor.fetchone()
                if result:
                    salary, raising = result
                    print(f"Salary: {salary}, Raising: {raising}")
                else:
                    print("No data found.")
            else:
                print("Invalid key. Try again")
                

    # Создание экземпляра класса User и вызов метода login_user
    user_instance = User()
    random_key = user_instance.login_user()
    print(random_key)

    # Проверка, что random_key существует, и создание экземпляра класса Info
    if random_key:
        user_info = Info(user_instance.login, user_instance.password, random_key)
        user_info.check_info()

connection.close()