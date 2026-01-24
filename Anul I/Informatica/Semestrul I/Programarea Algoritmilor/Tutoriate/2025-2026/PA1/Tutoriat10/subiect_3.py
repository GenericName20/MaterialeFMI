# SUBIECTUL 3 - PROGRAMARE DINAMICA

   """
    Descriere algoritm:
    Folosim Programarea Dinamică.
    Definim vectorul dp[i] = câștigul maxim ce se poate obține pentru o bară de lungime i.
    Relația de recurență:
    dp[i] = max(dp[i - lungime_k] + pret_k) pentru toate bucățile k, unde lungime_k <= i.
    
    Pentru reconstituirea soluției, folosim un vector 'tata' (sau 'last_cut') unde memorăm 
    ce lungime am tăiat ultima oară pentru a ajunge la optimul dp[i].
    
    Complexitate:
    Avem un vector de lungime L. Pentru fiecare poziție iterăm prin k tipuri de tăieturi.
    Complexitate Timp: O(k * L) - conform cerinței.
    Complexitate Spațiu: O(L).
  """

def solve_dp():
    # Citire date (simplu, ca in cerinta)
    L, k = map(int, input().split())
    lungimi = list(map(int, input().split()))
    preturi = list(map(int, input().split()))

    # dp[i] = castig maxim pentru lungimea i
    dp = [0] * (L + 1)
    # last[i] = ultima lungime folosita ca sa obtinem dp[i]
    last = [0] * (L + 1)

    # Programare dinamica (unbounded knap / rod cutting)
    for i in range(1, L + 1):
        best = -1
        best_len = 0
        for j in range(k):
            l = lungimi[j]
            p = preturi[j]
            if i >= l:
                val = dp[i - l] + p
                if val > best:
                    best = val
                    best_len = l
        dp[i] = best
        last[i] = best_len

    # Afisare castig maxim
    print(dp[L])

    # Reconstituire solutie
    sol = []
    x = L
    while x > 0:
        sol.append(last[x])
        x -= last[x]

    sol.sort()  
    print(*sol)




