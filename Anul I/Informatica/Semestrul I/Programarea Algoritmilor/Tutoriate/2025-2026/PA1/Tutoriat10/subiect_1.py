# SUBIECTUL 1 – Programarea Algoritmilor Examen

# a) Functia consoane_comune
def consoane_comune(*args):
    """
    Primeste un numar variabil de cuvinte si returneaza numarul maxim de cuvinte
    care au exact aceeasi multime de consoane.
    """
    def get_consoane(cuvant):
        vocale = "aeiouAEIOU"
        # Multimea consoanelor distincte din cuvant
        # tuple - este hashable(il putem folosi ca si cheie)
        return tuple(sorted({c for c in cuvant if c.isalpha() and c not in vocale}))

    frecventa = {}

    for cuv in args:
        cheie = get_consoane(cuv)
        frecventa[cheie] = frecventa.get(cheie, 0) + 1

    # Daca nu exista cuvinte, returnam 0
    return max(frecventa.values(), default=0)

# varainta 2: cu o singura functie
def consoane_comune(*args):
    vocale = "aeiouAEIOU"
    frecventa = {}

    for cuv in args:
        # multimea consoanelor din cuvant
        consoane = {c for c in cuv if c.isalpha() and c not in vocale}

        # transformam in tuple sortat pentru a putea fi cheie de dictionar
        cheie = tuple(sorted(consoane))

        frecventa[cheie] = frecventa.get(cheie, 0) + 1

    return max(frecventa.values(), default=0)



# b) List comprehension pentru prefix_5
# prefix_5 contine numerele care nu sunt multipli de 5
# si niciun prefix al lor nu este multiplu de 5
prefix_5 = [
    x for x in lista_numere
    if x % 5 != 0 and all(int(str(x)[:i]) % 5 != 0 for i in range(1, len(str(x))))
]


## c) Analiza complexității folosind Teorema Master



