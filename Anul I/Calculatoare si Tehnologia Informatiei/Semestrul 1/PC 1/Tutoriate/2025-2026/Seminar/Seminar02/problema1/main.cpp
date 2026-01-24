#include <iostream>

using namespace std;

#define nmax 1e5+1

struct persoana{
    long long CNP;
    string nume,prenume,stareC,adresa;
}v[nmax];

int main()
{
    int n;
    cin>>n;
    for(int i=1;i<=n;i++){
        cin>>v.CNP>>v.nume>>v.prenume>>v.stareC>>v.adresa;
        cout<<" "<<v.CNP<<" "<<v.nume<<" "<<v.prenume<<" "<<v.stareC<<" "<<v.adresa;
    }
    return 0;
}
