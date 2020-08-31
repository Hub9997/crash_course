sandwich_orders = ['cheese', 'pastrami', 'pastrami', 'onion', 'pastrami', 'salad', 'chicken']
finished_sandwiches = []
print('Deli has run out of pastrami.')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)

print("All sandwiches: ")
for san in finished_sandwiches:
    print(" Your sandwich with " + san + " is ready.")

print("--------------------------------")

places = {}
polling_active = True

while polling_active:
    name = input("\nWhat's your name?: ")
    response = input("\nWhere would you go ?")
    places[name] = response

    repeat = input("\nWould you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False

    # polling is complete, show the results
    print("\n---Polling is complete---")

    for name, response in places.items():
        print(name + "  you like to go to  " + response + ".")

print(" If you could visit one place, where would you go ?")

V = ['a', 'e', 'i', 'o', 'u']

s = 'azcbobobegghakl'

x = sum([1 for i in s if i in V])
print('Number of vowels: ' + str(x))
