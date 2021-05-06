class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over.")


my_dog = Dog('Amba', 11)
print("My dog is " + my_dog.name + ".")
print("My dog is " + str(my_dog.age) + "years old.")

my_dog.sit()
my_dog.roll_over()
print("_____________________")


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + " is a restaurant, that serves " + self.cuisine_type + " kuchnia.")

    def open_restaurant(self):
        print(self.restaurant_name + " is now open.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self,additional_served):
        self.number_served+=additional_served



restaurant = Restaurant("Newska", "Polska")
restaurant.describe_restaurant()
print("Number served is : " + str(restaurant.number_served))
restaurant.number_served = 277
print("\n Number served " + str(restaurant.number_served))
restaurant.open_restaurant()
restaurant.increment_number_served(237)
print("\n Number served " + str(restaurant.number_served))


restaurant2 = Restaurant("Hilary dla przyjaciol", "rybna-")
restaurant2.describe_restaurant()

restaurant3 = Restaurant("Fala", " stare ryby")
restaurant3.describe_restaurant()
restaurant2.open_restaurant()
print("_____________________")


class User():
    def __init__(self, first_name, last_name, age, occupation):
        self.first_nam = first_name
        self.last_name = last_name
        self.ag = age
        self.occupation = occupation

    def describe_user(self):
        print("User " + self.first_nam.title() + " " + self.last_name.title() +
              " of age  " + str(self.ag) + ", " + self.occupation + " is now in our team.")

    def greet_user(self):
        print("Hello " + self.first_nam.title() + ".")


user1 = User('janek', 'kowalski', 25, 'rolnik')

user1.describe_user()
user1.greet_user()
