# SUBIECTUL 2 - GREEDY

 """
    Descriere algoritm:
    Folosim metoda Greedy. Sortăm mașinile crescător după necesarul de benzină și 
    canistrele crescător după capacitate.
    Parcurgem mașinile și pentru fiecare încercăm să găsim cea mai mică canistră disponibilă
    care satisface nevoia (capacitate >= necesar).
    
    Complexitate:
    - Sortare mașini: O(N log N)
    - Sortare canistre: O(M log M)
    - Parcurgere liniară (merge-like): O(N + M)
    Complexitate totală: O(N log N) (presupunând N și M comparabile), care se încadrează în cerință.
"""

def greedy():
    # Citire date
    n = int(input())
    M = [int(input()) for _ in range(n)]

    m = int(input())
    C = [int(input()) for _ in range(m)]

    # Salvam (valoare, index) pentru afisare
    masini = [(M[i], i + 1) for i in range(n)]
    canistre = [(C[i], i + 1) for i in range(m)]

    # Sortare (pasul Greedy)
    masini.sort()      # dupa nevoie
    canistre.sort()    # dupa capacitate

    alocare = {}
    j = 0  # index pentru canistre

    for nevoie, id_m in masini:
        while j < m and canistre[j][0] < nevoie:
            j += 1

        if j == m:
            break

        alocare[id_m] = canistre[j][1]
        j += 1

    # Afisare rezultate
    print(len(alocare))
    for i in range(1, n + 1):
        if i in alocare:
            print(f"M{i} -> C{alocare[i]}")
        else:
            print(f"M{i} -> niciuna")


