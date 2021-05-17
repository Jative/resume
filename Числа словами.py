n1 = {"1": "один", "2": "два", "3": "три", "4": "четыре", "5": "пять",
      "6": "шесть", "7": "семь", "8": "восемь", "9": "девять"}
n1_1 = {"1": "одна", "2": "две", "3": "три", "4": "четыре",
        "5": "пять", "6": "шесть", "7": "семь", "8": "восемь", "9": "девять"}
n2 = {"1": "десять", "2": "двадцать", "3": "тридцать", "4": "сорок", "5": "пятьдесят",
      "6": "шестьдесят", "7": "семьдесят", "8": "восемьдесят", "9": "девяносто"}
n3 = {"1": "сто", "2": "двести", "3": "триста", "4": "четыреста", "5": "пятьсот",
      "6": "шестьсот", "7": "семьсот", "8": "восемьсот", "9": "девятьсот"}

tens = {"1": "одиннадцать", "2": "двенадцать", "3": "тринадцать", "4": "четырнадцать",
        "5": "пятнадцать", "6": "шестнадцать", "7": "семнадцать", "8": "восемнадцать", "9": "девятнадцать"}
thousands = ['тысяча', 'тысячи', 'тысяч']
millions = ['миллион', 'миллиона', 'миллионов']
billions = ['миллиард', 'миллиарда', 'миллиардов']
trillions = ['триллион', 'триллиона', 'триллионов']
quadrillions = ['квадриллион', 'квадриллиона', 'квадриллионов']
quintillions = ['квинтиллион', 'квинтиллиона', 'квинтиллионов']
sextillions = ['секстиллион', 'секстиллиона', 'секстиллионов']
septillions = ['септиллион', 'септиллиона', 'септиллионов']
octillions = ['октиллион', 'октиллиона', 'октиллионов']
nonillions = ['нониллион', 'нониллиона', 'нониллионов']
decillions = ['дециллион', 'дециллиона', 'дециллионов']

big_integers = (thousands, millions, billions, trillions, quadrillions, quintillions,
                sextillions, septillions, octillions, nonillions, decillions)
alls = [n1, n2, n3, n1_1, n2, n3]

for big_integer in big_integers[1:]:
    alls.extend([n1, n2, n3])

inp = input("Введите число: ")[::-1].replace(" ", "")
helper = inp
helper += "22"

if inp == "0"*len(inp):
    print("Ноль")
    input()
    quit()

if len(inp) == 0:
    print("Нужно ввести любое число")
    input()
    quit()

for symb in inp:
    if symb not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
        print("Нужно ввести число!")
        input()
        quit()

if len(inp) > len(alls):
    print("Введите число покороче, с такими большими я работать не умею")
    input()
    quit()

final = []

for ind in range(len(inp)):
    if ind % 3 == 0 and ind != 0 and int(helper[ind]) != 0 and int(helper[ind+1]) != 0 and int(helper[ind+2]) != 0:
        if inp[ind] == "1" and helper[ind + 1] != "1":
            big_number = big_integers[int(ind / 3 - 1)][0]
        elif inp[ind] in ("2", "3", "4") and helper[ind + 1] != "1":
            big_number = big_integers[int(ind / 3 - 1)][1]
        else:
            big_number = big_integers[int(ind / 3 - 1)][2]
        final.append(big_number)

    integer = alls[ind].get(inp[ind])
    if integer == "десять" and inp[ind-1] != "0":
        del final[-1]
        bombaster = inp[ind - 1]
        integer = tens.get(bombaster)
    if integer != None:
        final.append(integer)

final.reverse()
final[0] = final[0].title()
final = " ".join(final)
print(final)
input()
