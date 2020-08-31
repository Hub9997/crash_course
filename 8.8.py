def makealbum(name, title):
    album = name + ' ' + title
    return album.title()


while True:
    name = input("Please write album name: ")
    if name == 'q':
        break

    title = input("Please album title: ")
    if title == 'q':
        break

    album = makealbum(name, title)
print("\nYOur album " + ' ' + album)
