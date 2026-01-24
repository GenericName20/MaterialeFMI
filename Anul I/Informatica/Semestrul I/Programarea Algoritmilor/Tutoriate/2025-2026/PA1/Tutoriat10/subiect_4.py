# SUBIECT 4

def solve_backtracking():
    n, p = map(int, input().split())

    sol = []
    cnt = [0] * 10      # cnt[d] = de cate ori am folosit cifra d (1..9)
    total = 0

    def back():
        nonlocal total

        if len(sol) == n:
            print("".join(map(str, sol)))
            total += 1
            return

        for d in range(1, 10):
            # fara doua cifre alaturate egale
            if sol and sol[-1] == d:
                continue

            # fiecare cifra apare cel mult p ori
            if cnt[d] == p:
                continue

            sol.append(d)
            cnt[d] += 1

            back()

            cnt[d] -= 1
            sol.pop()

    back()
    print(total)


solve_backtracking()

