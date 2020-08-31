def make_sandwich(*added):
    print("I want sandwich with: ", *added)


make_sandwich('Ze serem')
make_sandwich('Ze serem i szynko',' + z jajkem.')

user_profile = {'first name': 'albert', 'last name': 'einstein', 'location': 'princeton', 'field': 'physics'}


def build_profile(first, last, **rozne):
    print("Moje dane to: ")
    profil = {}
    profil['first name'] = first
    profil['last name'] = last
    for key, value in rozne.items():
        profil[key] = value
    return profil


print(build_profile('Hubcio', 'Kulczyx', zawod='informatyk', dodatkowo='uzdrowiciel'))
#build_profile(user_prifil)

def make_car(marka,model,**other):
    car = {}
    car['marka'] = marka
    car['model'] = model
    for key,value in other.items():
        car[key]=value
    return car
car = make_car('subaru','outback',color = 'blue',tow_package = True)
print(car)