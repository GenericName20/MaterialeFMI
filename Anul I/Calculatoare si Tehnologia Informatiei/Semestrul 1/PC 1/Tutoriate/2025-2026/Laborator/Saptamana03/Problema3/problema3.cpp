#include <stdio.h>
#include <string.h>

char a[25],b[25],c[25];

int main() {
    int n=0;
    scanf("%s",a);
    scanf("%s",b);
    if (strlen(a)>=strlen(b))
        n=strlen(a);
    if (strlen(a)<strlen(b))
        n=strlen(b);
    memset(c, '0', n+1);
    c[n + 1] = '\0';
    if (strlen(a)<strlen(b)) {
        char temp[20];
        strcpy(temp,a);
        strcpy(a,b);
        strcpy(b,temp);
    }
    while (strlen(a) > strlen(b)) {
        memmove(b + 2, b + 1, strlen(b));
        b[1] = '0';
    }

    if (a[0]=='+' && b[0]=='+') {
        for (int i=strlen(a)-1;i>0;i--) {
            int val = a[i] -'0' + b[i] - '0' + c[i]-'0';
            c[i]=val%10+'0';
            c[i-1]=val/10+'0';
        }
        printf("%c",'+');
        int incep = 0;
        for (int i = 0; i < n ; i++) {
            if (c[i] != '0') incep = 1;
            if (incep) printf("%c", c[i]);
        }
    }
    if ((a[0] == '+' && b[0] == '-') || (a[0] == '-' && b[0] == '+')) {
        int cmp = 0;
        if (strlen(a) > strlen(b)) {
            cmp = 1;
        } else if (strlen(a) < strlen(b)) {
            cmp = -1;
        } else {
            if (strcmp(a + 1, b + 1) > 0) {
                cmp = 1;
            } else if (strcmp(a + 1, b + 1) < 0) {
                cmp = -1;
            } else {
                cmp = 0;
            }
        }
        char signResult = '+';
        if (cmp == 0) {
            printf("0");
            return 0;
        }
        if (cmp > 0) {
            signResult = a[0];
        } else {
            signResult = b[0];
        }
        char larger[25], smaller[25];
        if (cmp > 0) {
            strcpy(larger, a);
            strcpy(smaller, b);
        } else {
            strcpy(larger, b);
            strcpy(smaller, a);
        }
        for (int i = strlen(larger) - 1; i > 0; i--) {
            int val = (larger[i] - '0') - (smaller[i] - '0');
            if (val < 0) {
                larger[i - 1]--;
                val += 10;
            }
            c[i] = val + '0';
        }
        printf("%c", signResult);
        int incep = 0;
        for (int i = 1; i < n; i++) {
            if (c[i] != '0') {
                incep = 1;
            }
            if (incep) {
                printf("%c", c[i]);
            }
        }
    }
    return 0;
}
