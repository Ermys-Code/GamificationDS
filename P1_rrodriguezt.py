import inflect

p = inflect.engine()
numList = []
suma = 0
sumaMulti = 0

def AskNumbers():
    global numList
    flag = True
    while flag:
        num = int(input("Input a 2 characters number (0 for stop input): "))
        if len(str(num)) != 2:
            flag = False
        else:
            numList.append(num)

AskNumbers()

for i in range(len(numList)):
    suma += numList[i-1]
print(f"\nThe sum of all the elements in the list is {p.number_to_words(suma)}.")

for i in range(len(numList)):
    sumaMulti += numList[i-1] * 9
print(f"\nThe sum of all the elements multiplied by nine is {p.number_to_words(sumaMulti)}.")

numList = sorted(numList)

print(f"\nThe highest number in the list is {p.number_to_words(numList[-1])}.")
print(f"\nThe lowest number in the list is {p.number_to_words(numList[0])}.")
print(f"\nThe lenght of the list is {p.number_to_words(len(numList))}.")