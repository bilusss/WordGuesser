f = open('slowa.txt', 'r')

lines = f.readlines()
T = []
print("Jesli TAK to T, jesli NIE to N")
numbercheck = str(input("Czy chcesz podac ilosc liter?\n"))
startcheck = str(input("Czy chcesz podac na jaka/jakie zaczyna sie wyraz?\n"))
endcheck = str(input("Czy chcesz podac na jaka/jakie konczy sie wyraz?\n"))

if numbercheck == "T":
    numberofletters = int(input("Podaj liczbe liter wyrazu jaki chcesz dostac: "))
if startcheck == "T":
    startletters = str(input("Podaj litery zaczynajace wyraz jaki chcesz dostac: "))
if endcheck == "T":
    endletters = str(input("Podaj litery konczace wyraz jaki chcesz dostac: "))

if numbercheck == "T":
    numbercheck = True
else:
    numbercheck = False
if startcheck == "T":
    startcheck = True
else:
    startcheck = False
if endcheck == "T":
    endcheck = True
else:
    endcheck = False

print("\nTwoje kryteria to:")
if numbercheck:
    print(f"Liczba liter: {numberofletters}")
if startcheck:
    print(f"Zaczyna sie na: {startletters}")
if endcheck:
    print(f"Konczy sie na: {endletters}")

for word in lines:
    word = word.strip()
    flag = True
    # ///////////////// OPTYMALIZACJA
    if startcheck:
        if len(startletters) > len(word):
            continue
        if word[0] != startletters[0]:
            continue

    if endcheck:
        if len(endletters) > len(word):
            continue
        if word[-1] != endletters[-1]:
            continue
    # ///////////////// LICZBA LITER
    if numbercheck:
        if numberofletters != len(word):
            flag = False
    # ///////////////// POCZATEK
    if startcheck:
        i = 0
        wordstart = ""
        while i < len(startletters):
            wordstart += word[i]
            i += 1
        i = 0
        while i < len(startletters):
            if wordstart[i] != startletters[i]:
                flag = False
            i += 1
    # ///////////////// KONIEC
    if endcheck:
        i = 0
        wordend = ""
        while i < len(endletters):
            wordend += word[-1-i]
            i += 1
        i = 0
        while i < len(endletters):
            if wordend[i] != endletters[i]:
                flag = False
            i += 1
    if flag:
        T.append(word)

print(T)
f.close()