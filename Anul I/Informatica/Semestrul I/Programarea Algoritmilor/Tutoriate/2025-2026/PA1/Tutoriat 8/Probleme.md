# Probleme 

## Problema 1

Se dă un șir cu `n` numere întregi. Determinați cel mai mare număr care
poate fi obținut ca produs al două elemente ale șirului.

**Intrare**

```
7
-8 3 9 -1 -2 7 -10

```
**Ieșire**

```
80
```

------------------------------------------------------------------------

## Problema 2

În curtea unui atelier auto se află `n` mașini care trebuie reparate.
Deoarece există un singur mecanic, se poate lucra doar la o mașină la un
moment dat. Determinați numărul maxim de mașini ce pot fi reparate
într-un timp total `T`.

**masini.in**
```
5 10
6 2 4 8 2
```

**masini.out**

```
3
```
**Explicație:** Se repară mașinile cu timpii 2, 4 și 2.

------------------------------------------------------------------------

## Problema 3

Moș Crăciun pregătește cadourile pentru acest an. El cunoaște prețurile a `n` cadouri și are la dispoziție o sumă de bani `S`. Ajutați-l să aleagă un număr maxim de cadouri a căror preț total să nu depășească `S` și determinați suma minimă de care mai are nevoie Moș Crăciun pentru a cumpăra încă un cadou.

Programul citește de la tastatură numerele `n` `S`, iar apoi `n` numere naturale, reprezentând prețurile cadourilor.

Programul va afișa pe ecran două numere, `k` `p`, separate printr-un spațiu, reprezentând numărul maxim de cadouri pe care le poate cumpăra Moș Crăciun și suma minimă de care mai are nevoie pentru a cumpăra încă un cadou.

**Intrare**

```
5 10
7 2 6 4 3
```

**Ieșire**
```
3 5
```
**Explicație:** Cu suma dată Moș Crăciun va cumpăra trei cadouri, cele cu prețurile `2` `4` `3`. Mai are nevoie de încă `5` (bani) pentru a putea cumăra și cadoul cu prețul `6`.


------------------------------------------------------------------------

## Problema 4

La un birou care se ocupă cu analiza proiectelor de investiţii, `n` investitori au depus până la termenul legal, câte un proiect.
Cunoscând timpul necesar pentru analizarea fiecărui proiect, scrieţi un program care determină ordinea în care vor fi analizate proiectele, astfel încât timpul mediu de aşteptare pentru investitori să fie minim.

Pe prima linie a fişierului `proiecte.in` se găseşte un număr natural `n` reprezentând numărul de proiecte depuse.

Pe linia a doua, separate prin câte un spaţiu, se găsesc n numere naturale `t1`, `t2`, …, `tn`, reprezentând timpii necesari pentru analizarea fiecărui proiect.

Pe prima linie a fişierului `proiecte.out` se vor găsi n numere naturale cuprinse între 1 şi n, reprezentând ordinea în care vor fi analizate proiectele.


**proiecte.in**
```
5
60 50 30 10 40 
```

**proiecte.out**

```
4 3 5 2 1
```
**Explicație:** `4` `3` `5` `2` `1` este ordinea de analizare a proiectelor. Numerele de ordine ale proiectelor sunt date de ordinea numerelor de pe linia a doua din fişierul de intrare.


------------------------------------------------------------------------

## Problema 5

Pentru cadourile pe care Moş Crăciun urmează să le cumpere copiilor cuminţi, Consiliul Polului Nord a alocat suma de `S` eureni. Ştiind că în comerţul polar se utilizează `n+1` tipuri de bancnote de valori `1`, `e^1`, `e^2`, `e^3`,…, `e^n` şi faptul că Moşul trebuie să primească un număr minim de bancnote pentru suma aprobată, să se determine numărul de bancnote din fiecare tip utilizat în plata sumei şi numărul total de bancnote care i s-au alocat.

Fișierul de intrare `eureni.in` conține pe prima linie numerele naturale `S` `n` `e`.

Fișierul de ieșire `eureni.out` va conține mai multe linii: pe fiecare linie va fi scrisă valoare unei bancnote folosită în plata sumei `S` și numărul de bancnote folosite, separate printr-un spațiu, în ordinea descrescătoare a valorilor bancnotelor folosite. Pe ultima linie se va scrie numai numărul total de bancnote folosite.

**eureni.in**
```
107 4 5
```

**eureni.out**

```
25 4
5 1
1 2
7
```
**Explicație:** Sunt `5` tipuri de bancnote, cu valorile: `1`, `5`, `25`, `125`, `625` eureni. Pentru a plăti suma de `107` eureni se folosesc `4` bancnote de `25` eureni, `1` bancnotă de `5` eureni și `2` bancnote de `1` euren, în total `7` bancnote.

------------------------------------------------------------------------

## Problema 6


Gigel tocmai a învățat la școală adunarea și înmulțirea numerelor întregi. Pentru a-l ajuta pe Gigel să-și fixeze cunoștințele proaspăt dobândite, precum și pentru a-i testa istețimea algoritmică, bunicul său a scris pe mai multe cartonașe numere întregi nenule și apoi le-a împărțit în două grămezi: o grămadă `A` formată din `m` cartonașe și o grămadă `B` formată din `n` cartonașe (`1 ≤ m ≤ n ≤ 100000`). Sarcina lui Gigel este să selecteze din grămada `B` exact `m` cartonașe pe care apoi să le împerecheze, în orice ordine dorește el, cu cele `m` cartonașe din grămada `A` astfel încât prin însumarea produselor celor două numere scrise pe fiecare pereche de cartonașe să obțină cea mai mare sumă posibilă. Scrieți un program Python care citește de la tastatură valorile scrise pe cartonașele din cele două grămezi și afișează pe ecran cea mai mare sumă pe care o poate obține Gigel respectând restricțiile indicate în enunțul problemei, precum și o modalitate de obținere a sa în forma indicată în exemplu.

**Intrare**
```
A = [3, −2, 5, −1, 4]
B = [7, 8, −5, 2, −4, −1, 5]
```

**Ieșire**
```
97
```
**Explicație:** Suma maximă pe care o poate obține Gigel este  97 = -2 * -5 + -1 * -4 + 5 * 8 + 4 * 7 + 3 * 5

------------------------------------------------------------------------

## Problema 7

Considerăm `n` găleți pline cu apă. Acestea au o proprietate specială: capacitatea oricărei găleți (cu excepția celei cu capacitate minimă) este strict mai mare decât suma capacităților tuturor găleților mai mici decât ea.Se dă un bazin cu o capacitate `C`. Scrieți un program Python care determină ce găleți trebuie deșertate în bazin pentru a-l umple complet (exact la capacitatea `C`). Dacă acest lucru nu este posibil, se va afișa un mesaj corespunzător.

De la tastatură se citesc: o listă cu numere naturale nenule, reprezentând capacitățile celor `n` găleți si un număr natural nenul `C`, reprezentând capacitatea bazinului.

Programul va afișa: capacitățile găleților care, însumate, dau exact valoarea `C` sau un mesaj corespunzător (ex: "Nu este posibil") dacă bazinul nu poate fi umplut complet folosind gălețile date.

**Intrare**
```
30 6 62 5 133 14
153
```

**Ieșire**
```
14 6 133
```
------------------------------------------------------------------------

## Problema 8

În vitrina magazinului CheapLuxury, bijuteriile sunt așezate pe o matrice cu `m` rânduri și `n` coloane (`m>2`, `n>2`). Hoțul Gicuță vrea să fure câte o singură bijuterie de pe fiecare dintre cele `m` rânduri, astfel încât:
*1.* Valoarea totală a bijuteriilor furate să fie maximă.
*2.* Să respecte o regulă de "lăcomie": valoarea bijuteriei de pe rândul curent trebuie să fie strict mai mare decât valoarea bijuteriei furate de pe rândul precedent.
Scrieți un program Python care determină suma totală maximă și pozițiile bijuteriilor alese, respectând condițiile.(Notă: Pentru a maximiza suma totală respectând lanțul crescător de sus în jos, o strategie Greedy eficientă este adesea abordarea problemei în sens invers, de la ultimul rând spre primul).

**Intrare**
```
4 3
515.99 350.79 731.25
299.99 515.88 766.10
566.25 271.99 444.89
865.99 918.55 799.99
```

**Ieșire**
```
2351.47
1 2
2 2
3 1
4 2
```

------------------------------------------------------------------------

## Problema 9

Se organizează un concurs de trivia în Python la care participă Nea Vasile și alți `N` oameni. Fiecărui concurent i se asociază o valoare strict pozitivă $X_i$, cu excepția lui Vasile care are valoarea `0` (fiind subestimat).
Concursul are mai multe runde eliminatorii. Într-o rundă cu `K` participanți (inclusiv Vasile), sunt eliminați cei care greșesc, iar scorul rundei este:

$$ \text{Scor} = \frac{\text{Suma valorilor } X_i \text{ ale celor eliminați}}{K} $$

Câștigătorul primește suma scorurilor tuturor rundelor. Știind că Nea Vasile nu poate pierde și va rămâne singurul câștigător, el vrea să maximizeze câștigul total.Scrieți un program Python care determină suma maximă de bani pe care o poate câștiga Nea Vasile.

De la tastatură se citesc: un număr natural nenul `N`, reprezentând numărul de concurenți (fără Nea Vasile) si cele `N` numere strict pozitive asociate celor `N` participanți (separate prin spațiu).

Programul va afișa: Un singur număr real (cu 3 zecimale), reprezentând suma maximă de bani pe care o poate câștiga Nea Vasile.

**Intrare**
```
2
6 6
```

**Ieșire**
```
5
```

**Explicație:** Suma maximă este `5 = 2 + 3`. La început sunt `3` participanți (`N=2` adversari + Vasile).
*Runda 1* : Iese un singur adversar cu valoarea `6`. Număr participanți `K=3`. Scor: `6 / 3 = 2`.
Rămân `2` participanți (1 adversar + Vasile).
*Runda 2* : Iese ultimul adversar cu valoarea `6`. Număr participanți `K=2`. Scor: `6 / 2 = 3`.Total: `2 + 3 = 5`.

------------------------------------------------------------------------

## Problema 10

Canalul Pythonic Way este foarte strâmt, având o serie de nuferi așezați liniar, numerotați de la `1` la `n`. Pe fiecare nufăr cu indicele `i` este scris un număr natural nenul `k`, care reprezintă puterea de salt a broscuței de pe acel nufăr.Mai exact, de pe nufărul `i` având valoarea `k`, broscuța poate sări pe oricare dintre nuferii cu indicii `i+1`, `i+2`, ..., `i+k`.Broscuța Lily vrea să plece de pe primul nufăr (indice `1`) și să ajungă pe ultimul nufăr (indice `n`) efectuând un număr minim de sărituri.Scrieți un program Python care determină și afișează un astfel de traseu minim.
Dacă există mai multe trasee cu număr minim de sărituri, se poate afișa oricare dintre ele.Broscuța se oprește imediat ce a ajuns pe ultimul nufăr.

De la tastatură se citesc, separate prin spațiu, numerele naturale scrise pe cei `n` nuferi (în ordinea de la `1` la `n`).
(Notă: Numărul total de nuferi `n` se deduce din numărul de valori citite).

Programul va afișa pe ecran indicii nuferilor pe care sare Lily pentru a ajunge de la început la sfârșit, separați prin câte un spațiu. Traseul trebuie să includă nufărul de start (`1`) și nufărul de final (`n`).

**Intrare**
```
2 3 1 5 3 2 2 5
```

**Ieșire**
```
1 2 4 8
```

*(Sau o altă variantă validă, de exemplu: `1 3 4 8`, deoarece de pe nufărul `1` se poate sări și pe `2`, și pe `3`, iar de pe ambele se poate ajunge optim la destinație).*

**Explicație:** Avem `n=8` nuferi cu valorile:
Nufăr `1` (valoare `2`): poate sări la `2`, `3`.
Nufăr `2` (valoare `3`): poate sări la `3`, `4`, `5`.
Nufăr `4` (valoare `5`): poate sări la `5`, `6`, `7`, `8`, `9`.
Lily alege traseul $1 \to 2 \to 4 \to 8$ 
Total sărituri: 3 (minim posibil).

------------------------------------------------------------------------

## Problema 11

O balanță veche s-a defectat și acum se echilibrează nu doar pentru două obiecte având aceeași greutate, ci pentru orice două obiecte cu proprietatea că modulul diferenței dintre greutățile lor este mai mic sau egal decât un număr real `g`.
Scrieți un program Python care citește de la tastatură:
1.Un număr natural `n` (numărul de obiecte).
2.Un număr real `g` (toleranța balanței).
3.Greutățile celor `n` obiecte (numere reale strict pozitive).

Programul va afișa pe ecran numărul maxim de perechi de obiecte care echilibrează balanța defectă, precum și perechile respective.
Orice obiect poate să facă parte din cel mult o pereche.
Fiecare pereche afișată trebuie să fie de forma `x + y`, unde `x` și `y` sunt numerele de ordine ale celor două obiecte (indexate de la 1).
Nu contează ordinea afișării perechilor sau ordinea numerelor în cadrul unei perechi.

De la tastatură se citesc: un număr natural `n`, un număr real `g` si o secvență de `n` numere reale reprezentând greutățile.

Programul va afișa:
Pe prima linie: Numărul maxim de perechi formate.
Pe următoarele linii: Perechile de indici în formatul `x + y`.

**Intrare**
```
10
8.5
21.25
12
6.05
20.7
23.8
22
33.25
21
48.15
62.20
```

**Ieșire**
```
3
3 + 2
10 + 4
1 + 8
```

**Explicație:** Avem $n = 10$ și $g = 8.5$. Se pot forma maxim 3 perechi de obiecte care pot echilibra balanța defectă. Soluția nu este unică, o altă soluție corectă obținându-se, de exemplu, înlocuind perechea $1 + 6$ cu perechea $1 + 5$ (în contextul unei alte variante de grupare).
