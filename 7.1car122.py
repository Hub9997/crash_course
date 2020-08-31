print("What kind of car would you like ?")
car = input()
print("Let me see, if I have "+ car +".")

print("How many people are in your group? ")
answer = int(input())
if answer >=8:
    print("You'll have to wait")
else:
    print("We have table for You .")

print("Please give me your number: ")
ans = input()
ans = int(ans)
if ans % 10==0:
    print("Jest podzielna przez 10")
else:
    print("Nie jest podzielna(isn't multiple of 10:(.)")

current_number=1
while current_number <=5:
    print(current_number)
    current_number+=1
print("--------------------------------")

current_number=1
while current_number <=5:
    print(current_number)
    if current_number ==4:
        break
    current_number+=1