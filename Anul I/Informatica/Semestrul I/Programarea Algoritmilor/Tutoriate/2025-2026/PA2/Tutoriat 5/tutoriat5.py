''' a) Pentru o listă, numim set de elemente al listei mulțimea elementelor
distincte ale sale (de exemplu setul de elemente al listei [3, 1, 3] este {1, 3}).
Scrieți o funcție set_elemente care primește ca parametru un număr variabil de liste și
returnează numărul maxim de liste dintre cele primite ca parametru care au același set de
elemente. De exemplu, apelul text{set\_elemente}([1, 3], [4, 5], [1, 3, 1], [5, 4, 5, 4],
[5, 4, 4]) returnează 3, corespunzător listelor [4, 5], [5, 4, 5, 4], [5, 4, 4]. (1.5 p.)
'''

def set_elemente(*liste):
    d = {}
    for lista in liste:
        set_lista = frozenset(lista) # tuple(set(lista))
        if set_lista not in d:
            d[set_lista] = 1
        else:
            d[set_lista] += 1

    max = 0
    for set_lista in d:
        if d[set_lista] > max:
            max = d[set_lista]

    return max


# apel
lista = [[1, 3], [4, 5], [1, 3, 1], [5, 4, 5, 4], [5, 4, 4]]
print(set_elemente(*lista))

set_elemente([1, 3], [4, 5], [1, 3, 1], [5, 4, 5, 4], [5, 4, 4])
'''b) Știind că lista_c este o listă de cuvinte (șiruri de caractere), înlocuiți punctele de
suspensie din instrucțiunea prima_litera = […] cu o secvență de inițializare (list comprehension) astfel încât, după executarea sa, lista prima_litera să conțină toate cuvintele din lista lista_c în care prima literă nu se repetă în interiorul cuvântului (are frecvența 1).

De exemplu, pentru lista_c = ['unul', 'dintre', 'subiecte', 'e', 'acesta'],
lista prima_litera va fi ['dintre', 'subiecte', 'e'].'''

lista_c = ['unul', 'dintre', 'subiecte', 'e', 'acesta']
prima_litera=[cuvant for cuvant in lista_c if cuvant.count(cuvant[0])==1]
print(prima_litera)

l=[1,2,2]
l.remove(2)
print(l)