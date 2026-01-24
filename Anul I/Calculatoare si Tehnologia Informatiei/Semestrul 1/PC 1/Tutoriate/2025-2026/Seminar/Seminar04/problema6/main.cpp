#include <stdio.h>


int conditie (int x){
    return (x%2 == 0);
}

int cautare (int n, int v[], int(*f)(int)){
    for (int i = 0; i<n; i++){
        if (f(v[i])){
            return i;
        }
    }
    return -1;
}


int main()
{
    int n, v[100];
    scanf ("%d", &n);
    for (int i = 0; i<n; i++){
        scanf ("%d", &v[i]);
    }
    int c = cautare (n, v, conditie);
    printf("%d", c);
    return 0;
}
