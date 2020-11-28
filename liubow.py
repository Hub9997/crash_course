filename = 'programming.txt'

with open(filename,'w') as file_object:
    file_object.write("Ja kocham programowanie.\n")
    file_object.write("Milosc nie cielesna, a swiadomosciowa:)\n")
with open(filename,'a') as file_object:
    file_object.write("Dodam jeszcze, ze spokoj wazny jest.")