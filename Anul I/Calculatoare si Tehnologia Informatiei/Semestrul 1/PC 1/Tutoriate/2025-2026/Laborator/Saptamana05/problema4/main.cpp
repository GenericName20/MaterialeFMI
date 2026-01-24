#include <bits/stdc++.h>

using namespace std;
ifstream in("caca.in");
ofstream out("caca.out");

int const nmax=5e1+1;

int n,m;

int a[nmax][nmax];
int b[nmax][nmax];
int r[nmax][nmax];

void Adunare(){
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            r[i][j]=a[i][j]+b[i][j];
        }
    }
}

void Inmultire(){
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            for(int h=1;h<=n;h++){
                for(int k=1;k<=n;k++){
                    r[i][j]+=a[h][k]*b[k][h];
                }
            }
        }
    }
}

void Afisare(){
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            out<<r[i][j]<<' ';
        }
        out<<'\n';
    }
}

int main(){
    string s;
    in>>s;
    in>>n>>m;
    for(int i=1;i<=n*m;i++){
        int x,y,z;
        in>>x>>y>>z;
        a[x][y]=z;
    }
    for(int i=1;i<=n*m;i++){
        int x,y,z;
        in>>x>>y>>z;
        b[x][y]=z;
    }
    if(s=="inmultire"){
        Inmultire();
        Afisare();
    }
    if(s=="adunare"){
        Adunare();
        Afisare();
    }
    return 0;
}
