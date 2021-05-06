from 
class Admin(User):

    def __init__(self, first_name, last_name, age, occupation):
        super().__init__(first_name, last_name, age, occupation)
        self.privileges = []

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("Admin's privileges are :" + privilege)


admin1 = Admin('Antoni', 'Jacyno', 44, 'nauczyciel informatyki')
admin1.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',

]
admin1.show_privileges()
admin1.describe_user()

user1 = User('janek', 'kowalski', 25, 'rolnik')
user1.describe_user()
user1.greet_user()
user1.login_attempts = 10
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print("Login attempts :" + str(user1.login_attempts))
user1.reset_login_attempts()
print("Login attempts :" + str(user1.login_attempts))

