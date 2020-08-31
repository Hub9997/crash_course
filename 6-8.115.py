pets = [{'dog':{'legs':4,'voice':'hau','food':'chappi'}},{'cat':{'legs':4,'voice':'miau','food':'kitikat'}},
        {'malpa':{'legs':2,'voice':'ua','food':'bananas'}}]
for pet in pets:
    print(pet)
pets[0]['dog']['voice'] = 'hauu'
print(pets)
print("________________________________________________")
print(pets[1])
print("****************************************************************")
for pet in pets:
  print(pet)


favorite_places = {
          'friend1': {
                       'first ': "Krakow",
                       'second': "Postolowo",
                       'third': 'Gdansk'
           },

           'friend2':{
    'first': 'Elganowo',
    'second': 'Skarszewy',
    'third': 'Leba'
},
           'friend3':{
    'first' : 'Pruszcz',
    'second' : 'Gdansk',
    'third' : 'Pruszcz Gdanski'
},
}
for item in favorite_places.items():
    print(item)

print("\n________________________________________")

for friend, place in favorite_places.items():
    print("\tFavorite places of " + friend + " are: ")
    print(favorite_places[friend])
