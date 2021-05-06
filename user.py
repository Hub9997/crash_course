class User():
    def __init__(self, first_name, last_name, age, occupation):
        self.first_nam = first_name
        self.last_name = last_name
        self.ag = age
        self.occupation = occupation
        self.login_attempts=0

    def describe_user(self):
        print("User " + self.first_nam.title() + " " + self.last_name.title() +
              " of age  " + str(self.ag) + ", " + self.occupation + " is now in our team.")

    def greet_user(self):
        print("Hello " + self.first_nam.title() + ".")

    def increment_login_attempts(self):
        self.login_attempts=self.login_attempts +1


    def reset_login_attempts(self):
        self.login_attempts=0



user1 = User('janek', 'kowalski', 25, 'rolnik')

user1.describe_user()
user1.greet_user()
user1.login_attempts =10
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print("Login attempts :" + str(user1.login_attempts))
user1.reset_login_attempts()
print("Login attempts :" + str(user1.login_attempts))