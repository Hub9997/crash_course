def make_shirt(size,text):
    print(f"This shirt is "+str(size) + " size. " + text)
make_shirt(5, "Bye.")
make_shirt(4,text = "Byebye.")
    #print(format())

def make_skirt(size=7,text="Biiig."):
    print("Wow,that skirt of size "+str(size)+" is veryy big. "+ text)
make_skirt()
make_skirt(size = 5)
make_skirt(size = 4,text = "I love Python.")

def describe_city(name,country):
    print("\nThe city "+name.title() + " is placed in  " + country.title()+".")

describe_city("warszawa","polska")
print("----------------------------------------")

def get_formatted_name(first_name, last_name):

    full_name = first_name +" "+last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


def build_person(first_name, last_name, age=''):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
musician = build_person('jimi','hendrix',age=27)
print(musician)



def city_country(city, country):
    place= city + country
    return place.title()
pierwszy =city_country("Warszawa,","Polska.")
print(pierwszy)