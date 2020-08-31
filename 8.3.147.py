unprinted_designs = ['iphon', 'robot', 'tetrahedron']
completed_models = []
while unprinted_designs:
    curreent_desing = unprinted_designs.pop()
    print("Printing model " + curreent_desing)
    completed_models.append(curreent_desing)

print("\nThe following models have been printed : ")
for completed_model in completed_models:
    print(completed_model)
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        curreent_desing=unprinted_designs.pop()

        print("Printing model"+curreent_desing)
        completed_models.append(curreent_desing)

def show_completed_models(completed_models):
    print("\nThe following models have been printed : ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphon', 'robot', 'tetrahedron']
completed_models=[]

def show_magicians():
  for magician in magicians:
    print(magician)

magicians = ["jan","arek"]
show_magicians()

def make_great():
 for magician in magicians:
   print("Great "+magician)
show_magicians()
make_great()