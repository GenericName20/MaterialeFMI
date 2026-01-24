#include <iostream>

using namespace std;

struct poo{
    short byte1:8;
    short byte2:8;
};

union foo{
    short nr;
    poo wow;
}caca;

void swip(foo &a)
{
    short aux;
    aux=a.wow.byte1;
    a.wow.byte1=a.wow.byte2;
    a.wow.byte2=aux;
}

int main()
{
    cin>>caca.nr;
    swip(caca);
    cout<<caca.nr<<'\n';
    swip(caca);
    cout<<caca.nr<<'\n';
    return 0;
}
