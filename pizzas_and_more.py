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