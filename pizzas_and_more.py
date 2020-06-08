warzywa = ['kalarepę', 'koper', 'rzodkiew']
for warzywo in warzywa:
    print("Lubię " + warzywo + ".\n")

print("Lubię wszystkie ciemno zielone warzywa")

my_list = ['auto1','auto2','auto3','dom1','dom2','dom3']
print('Pierwsze trzy rzeczy:')
print(my_list[0:3])

print("Srodkowe:")
print(my_list[1:5])

print("The last three items: ")
print(my_list[-3:])

friend_warzywas = warzywa[:]
print(friend_warzywas)

friend_warzywas.append('pomidor')
print(friend_warzywas)
print("My favorite warzywas are : "  )



moje = [warz for warz in warzywa]
print(moje)

print("And my friend likes : ")
jego = [warz for warz in friend_warzywas]
print(jego)
#write two for loops to print each list of food

miejsca = ['Hiszpania','Wlochy','Majorka','Tybet','Tajlandia']
print(miejsca)
print(sorted(miejsca))
print(miejsca)
miejsca.reverse()
print(miejsca)
miejsca.reverse()
print(miejsca)
miejsca.sort()
print(miejsca)

guests = ['Lukasz', 'Agnieszka','Mariola']
print(guests[0] +" I'm inviting You to a dinner.")
print(guests[1] +" I'm inviting You to a dinner.")
print(guests[2] +" I'm inviting You to a dinner.")
print(guests[1]+ " can't make it.")
guests[1] = 'Vardan'
print(len(guests))

print(guests[0] +" I'm inviting You to a dinner.")
print(guests[1] +" I'm inviting You to a dinner.")
print(guests[2] +" I'm inviting You to a dinner.")
print(" I've found a bigger table.")
guests.insert(1,'Ewelina')
print(guests)
guests.insert(2,'Ania')
print(guests[0] +" I'm inviting You to a dinner.")
print(guests[1] +" I'm inviting You to a dinner.")
print(guests)
guests.append('Kasia')
print(guests)
guests.pop()
print(guests)
guests.pop()
print(guests)
guests.pop()
print(guests)
guests.pop(0)
print(guests)
del guests[0]
print(guests)
del guests[0]
print(guests)
