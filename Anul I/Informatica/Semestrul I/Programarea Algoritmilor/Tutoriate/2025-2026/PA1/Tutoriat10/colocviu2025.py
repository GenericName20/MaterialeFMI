# COLOCVIU 2025 - Subiectul 1
# matrice.in -> matrice.out

def este_palindrom(x: int) -> bool:
    s = str(x)
    return s == s[::-1]


def main():
    # Citim matricea din fisier
    with open("matrice.in", "r") as f:
        mat = [list(map(int, line.split())) for line in f if line.strip()]

    # Stergem elementele palindroame din fiecare linie
    for i in range(len(mat)):
        mat[i] = [x for x in mat[i] if not este_palindrom(x)]

    # Gasim lungimea maxima a unei linii
    max_len = 0
    for row in mat:
        if len(row) > max_len:
            max_len = len(row)

    # Completam liniile mai scurte cu 0 la final
    for row in mat:
        while len(row) < max_len:
            row.append(0)

    # Scriem in fisierul matrice.out
    with open("matrice.out", "w") as g:
        for row in mat:
            g.write(" ".join(map(str, row)) + "\n")



# COLOCVIU 2025 - Subiectul 2
# restrans.in -> restrans.out

def expand(line: str) -> str:
    i = 0
    out = []

    while i < len(line):
        if line[i] == '(':
            # citim pana la ')'
            i += 1
            start = i
            while i < len(line) and line[i] != ')':
                i += 1
            seg = line[start:i]
            i += 1  # sarim peste ')'
        else:
            # citim litere pana la '(' sau cifra
            start = i
            while i < len(line) and line[i].isalpha():
                i += 1
            seg = line[start:i]

        # citim numarul (daca exista)
        start_num = i
        while i < len(line) and line[i].isdigit():
            i += 1

        if start_num < i:
            k = int(line[start_num:i])
        else:
            k = 1

        out.append(seg * k)

    return "".join(out)


def main():
    rezultate = []

    with open("restrans.in", "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            rezultate.append(expand(line))

    # scriem pe o singura linie, separate prin virgula
    with open("restrans.out", "w") as g:
        g.write(",".join(rezultate))



# COLOCVIU 2025 - Subiectul 3
# depozite.in

 # STRUCTURA
    """
    data = {
      "Banca Transilvania": {
          "LEI": [
              {"suma": 10000, "dobanda": 4.5, "perioada": 12},
              {"suma": 5000,  "dobanda": 4.0, "perioada": 6}
          ],
          "EURO": [
              {"suma": 2000, "dobanda": 2.0, "perioada": 12}
          ]
      },
      "ING Bank": {
          "DOLAR": [
              {"suma": 1500, "dobanda": 3.5, "perioada": 24}
          ],
          "LEI": [
              {"suma": 7000, "dobanda": 4.2, "perioada": 18},
              {"suma": 3000, "dobanda": 4.0, "perioada": 6}
          ]
      }
    }
    """

def citeste_depozite(nume_fisier="depozite.in"):
    # structura: data[bank][currency] = lista de depozite (dict)
    data = {}

    with open(nume_fisier, "r") as f:
        current_bank = None
        current_curr = None

        for line in f:
            line = line.strip()
            if not line:
                continue

            if line.startswith("Banca:"):
                # Exemplu: "Banca: Banca Transilvania , Moneda: LEI"
                # spargem in doua bucati: bank si moneda
                left, right = line.split(",")
                bank = left.split(":", 1)[1].strip()
                curr = right.split(":", 1)[1].strip()

                current_bank = bank
                current_curr = curr

                if current_bank not in data:
                    data[current_bank] = {}
                if current_curr not in data[current_bank]:
                    data[current_bank][current_curr] = []
            else:
                # linie de forma: suma dobanda perioada
                suma_s, dob_s, per_s = line.split()
                dep = {
                    "suma": int(suma_s),
                    "dobanda": float(dob_s),
                    "perioada": int(per_s)
                }
                data[current_bank][current_curr].append(dep)

    return data


def actualizeaza_depozite(data, *args):
    """
    Parametri in ordine (ca in cerinta):
    - structura data
    - numar variabil de banci (siruri)
    - moneda (sir)
    - p (float) procentul cu care se mareste dobanda
    - x (int) perioada minima (luni)
    """

    banci = args[:-3]
    moneda = args[-3]
    p = float(args[-2])
    x = int(args[-1])

    for banca in banci:
        if banca in data and moneda in data[banca]:
            for dep in data[banca][moneda]:
                if dep["perioada"] >= x:
                    dep["dobanda"] += p


def centralizator(data):
    # adunam pe monede: initial si final
    s_init = {}
    s_final = {}

    for banca in data:
        for moneda in data[banca]:
            for dep in data[banca][moneda]:
                suma = dep["suma"]
                dob = dep["dobanda"]
                s_init[moneda] = s_init.get(moneda, 0.0) + suma
                s_final[moneda] = s_final.get(moneda, 0.0) + suma * (1.0 + dob / 100.0)

    rez = []
    for moneda in s_init:
        init = round(s_init[moneda], 2)
        fin = round(s_final[moneda], 2)
        rez.append((moneda, init, fin))

    # sortare: descrescator dupa castig, apoi lexicografic dupa moneda
    rez.sort(key=lambda t: (-(t[2] - t[1]), t[0]))
    return rez


def main():
    data = citeste_depozite("depozite.in")

    # b) exemplu de apel (ca in enunt):
    actualizeaza_depozite(
        data,
        "Banca Transilvania",
        "Alpha Bank",
        "LEI",
        2,
        12
    )

    # afisam structura actualizata (simplu)
    print(data)

    # c) centralizator
    rez = centralizator(data)
    for moneda, init, fin in rez:
        print(f"Moneda {moneda}: suma initiala = {init:.2f}, suma finala = {fin:.2f}")



