#include <stdio.h>
#include <string.h>

int main()
{
    char s[100];
    scanf("%s",s); // citeste un sir de caractere (de exemplu un numar binar)
    int n=strlen(s); // lungimea sirului initial
    // calculeaza cate zerouri trebuie adaugate la inceput pentru ca lungimea sa fie multiplu de 4
    int extra=(4 - n % 4) % 4;
    char bin[120] = ""; // sirul final in care vom pune zerourile + s
    // adauga zerouri la inceputul sirului bin
    for (int i = 0; i < extra; i++)
        bin[i] = '0';
    // pune s dupa zerourile adaugate
    for (int i = extra; i < n + extra; i++)
        bin[i] = s[i - extra];
    // actualizeaza lungimea
    n += extra;
    // parcurge sirul binar cate 4 caractere (4 biti = 1 cifra hex)
    for (int i = 0; i < n; i = i + 4){
        int val = 0; // valoarea in baza 10 a celor 4 biti transforma cei 4 biti in valoare zecimala
        for (int j = 0; j < 4; j++)
            val = val * 2 + (bin[i + j] - '0');
        if (val < 10) // afiseaza cifra hex corespunzatoare
            printf("%d", val); // cifre 0-9
        else
            printf("%c", 'A' + (val - 10)); // litere A-F
    }
    return 0;
}
