magicians = ['Jan Kowalski','Zbyszek Piotrowski']
def show_magicians():
    for magician in magicians:
        print(magician)
show_magicians()


copy_magicians = magicians[:]

def make_great():
    for magician in copy_magicians:
        message ="The great " + magician +'.'
        print(message)


make_great()
print(magicians)
