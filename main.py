class ksiazka:
    def __init__(self, tytul, autor, rok):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok
        self.quantity = 1


class osoba:
    def __init__(self, imie):
        self.imie = imie
        self.pozyczonych = 0
        self.ksiazki = {}


n = input()
ksiazki = {}
ludzie = {}


def commands(command, tytul, autor, rok=None):
    def dodaj(tytul, autor, rok):
        if tytul in ksiazki:
            ksiazki[tytul].quantity += 1
        else:
            ksiazki[tytul] = ksiazka(tytul, autor, rok)
        return True

    def wypozycz(imie, tytul):
        if ludzie[imie].pozyczonych == 3:
            return False
        else:
            if tytul in ksiazki:
                if ksiazki[tytul].quantity >= 1 and tytul not in ludzie[imie].ksiazki:
                    ludzie[imie].pozyczonych += 1
                    ksiazki[tytul].quantity -= 1
                    ludzie[imie].ksiazki[tytul] = tytul
                    return True
            return False

    def donate(imie, tytul):
        if imie in ludzie:
            if tytul in ludzie[imie].ksiazki:
                ludzie[imie.wypozyczonych] -= 1
                ksiazki[tytuly].quantity += 1
                del ludzie[imie].ksiazki[tytul]
                return True
        return False

    if command == 'dodaj':
        return add(tytul, autor, rok)
    elif command == 'wypozycz':
        if tytul not in ludzie:
            ludzie[tytul] = osoba(tytul)
        return wypozycz(imie=tytul, tytul=autor)
    elif command == 'oddaj':
        return donate(imie=tytul, tytul=autor)


for i in range(int(n)):
    temp = eval(input())
    command = temp[0].strip()
    tytul = temp[1].strip()
    autor = temp[2].strip()
    if len(temp) > 3:
        year = temp[3]
        print(commands(command, tytul, autor, rok))
    else:
        print(commands(command, tytul, autor))