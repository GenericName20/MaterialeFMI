# 3. autori.in (structuri de date)

def citeste_autori(nume_fisier="autori.in"):
    with open(nume_fisier, "r") as f:
        m, n = map(int, f.readline().split())

        autori = {}
        for _ in range(m):
            parts = f.readline().split()
            cod = int(parts[0])
            nume = parts[1]
            prenume = parts[2]
            autori[cod] = f"{nume} {prenume}"

        carti_autor = {cod: [] for cod in autori}
        carte_to_autor = {}
        carte_info = {}

        for _ in range(n):
            linie = f.readline().rstrip("\n")
            parts = linie.split()
            cod_autor = int(parts[0])
            cod_carte = int(parts[1])
            an = int(parts[2])
            pag = int(parts[3])
            titlu = " ".join(parts[4:])

            carti_autor[cod_autor].append(cod_carte)
            carte_to_autor[cod_carte] = cod_autor
            carte_info[cod_carte] = (titlu, an, pag)

    return {
        "autori": autori,
        "carti_autor": carti_autor,
        "carte_to_autor": carte_to_autor,
        "carte_info": carte_info
    }


def sterge_carte(data, cod_carte):
    if cod_carte not in data["carte_to_autor"]:
        return None

    cod_autor = data["carte_to_autor"][cod_carte]
    nume_autor = data["autori"][cod_autor]

    # stergem din lista autorului
    data["carti_autor"][cod_autor].remove(cod_carte)

    # stergem mapping-urile
    del data["carte_to_autor"][cod_carte]
    del data["carte_info"][cod_carte]

    return nume_autor


def carti_autor(data, cod_autor):
    if cod_autor not in data["autori"]:
        return []  # cerinta: lista vida daca autorul nu exista

    nume_autor = data["autori"][cod_autor]
    rezultat = []

    for cod_carte in data["carti_autor"][cod_autor]:
        titlu, an, pag = data["carte_info"][cod_carte]
        rezultat.append((titlu, an, pag))

    # sortare: an cresc, pag desc, titlu cresc
    rezultat.sort(key=lambda x: (x[1], -x[2], x[0]))
    return nume_autor, rezultat


def main():
    data = citeste_autori("autori.in")

    # b) stergere carte
    cod_carte = int(input())
    autor = sterge_carte(data, cod_carte)

    if autor is None:
        print("Cartea nu exista.")
    else:
        print(f"Cartea a fost scrisa de {autor}.")

    print(data)  # "structura de date afisata"

    # c) carti autor
    cod_aut = int(input())
    rez = carti_autor(data, cod_aut)

    if rez == []:
        print("cod incorect")
    else:
        nume, carti = rez
        print(nume)
        for titlu, an, pag in carti:
            print(titlu, an, pag)


