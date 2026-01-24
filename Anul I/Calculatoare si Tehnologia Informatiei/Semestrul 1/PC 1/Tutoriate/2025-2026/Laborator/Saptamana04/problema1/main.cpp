#include <fstream>
#include <string>
#include <string.h>

using namespace std;

ifstream cin("test.in");
ofstream cout("test.out");

int const nmax=1005;

int i=0;
int admisi=0;

struct candidat{
    int nr_legitimatie;
    string nume;
    int nota_mate,nota_info,nota_bac,medie;
    char admis='N',buget='0';
}v[nmax];

int comparare(string s1,string s2)
{
    int j=0;
    while(j<min(s1.size(),s2.size()))
    {
        if(s1[j]-'0'==s2[j]-'0')
            j++;
        else
        if(s1[j]-'0'>s2[j]-'0')
            return 1;
        if(s1[j]-'0'<s2[j]-'0')
            return -1;
    }
    return -1;
}

void sorteaza_datele()
{
    for(int j=0;j<i-1;j++)
    {
        for(int h=0;h<i-1;h++)
        {
            if(comparare(v[h].nume,v[h+1].nume)>0)
                swap(v[h],v[h+1]);
        }
    }
}

void sorteaza_medie()
{
    for(int j=0;j<i-1;j++)
    {
        for(int h=0;h<i-1;h++)
        {
            if(v[h].medie<v[h+1].medie)
                swap(v[h],v[h+1]);
        }
    }
}

void adauga_elev(int a,string n,int b,int c,int d)
{
    v[i].admis='N';v[i].buget='0';
    v[i].nr_legitimatie=a;v[i].nume=n;
    v[i].nota_mate=b;v[i].nota_info=b;v[i].nota_bac=c;
    v[i].medie = ((v[i].nota_mate + v[i].nota_info)/2)*8;
    v[i].medie+=v[i].nota_bac*2;
    v[i].medie/=10;
    if(v[i].medie>=5)
    {
        admisi++;
        v[i].admis='Y';
    }
    i++;
    sorteaza_datele();
}


void Calculeaza_buget()
{
    sorteaza_medie();
    int j=admisi*3/4;
    for(int h=0;h<admisi*3/4;h++)
    {
        v[h].buget='Y';
    }
    for(j;j<admisi;j++)
    {
        v[j].buget='N';
    }
    sorteaza_datele();
}

void Afiseaza(int st,int dr,char c)
{
    for(int j=st;j<dr;j++)
    {
        if(c=='A')
            cout<<v[j].nr_legitimatie<<" "<<v[j].nume<<"\n"<<v[j].nota_mate<<" "<<v[j].nota_info<<" "<<v[j].nota_bac<<"\n"<<v[j].medie<<"\n"<<v[j].admis<<" "<<v[j].buget<<"\n\n";
        else
        if(c=='B' && v[j].buget=='Y')
            cout<<v[j].nr_legitimatie<<" "<<v[j].nume<<"\n"<<v[j].nota_mate<<" "<<v[j].nota_info<<" "<<v[j].nota_bac<<"\n"<<v[j].medie<<"\n"<<v[j].admis<<" "<<v[j].buget<<"\n\n";
        else
        if(c=='T' && v[j].buget=='N')
            cout<<v[j].nr_legitimatie<<" "<<v[j].nume<<"\n"<<v[j].nota_mate<<" "<<v[j].nota_info<<" "<<v[j].nota_bac<<"\n"<<v[j].medie<<"\n"<<v[j].admis<<" "<<v[j].buget<<"\n\n";
        else
        if(c=='R' && v[j].buget=='0')
            cout<<v[j].nr_legitimatie<<" "<<v[j].nume<<"\n"<<v[j].nota_mate<<" "<<v[j].nota_info<<" "<<v[j].nota_bac<<"\n"<<v[j].medie<<"\n"<<v[j].admis<<" "<<v[j].buget<<"\n\n";
    }
}

void Afiseaza_cumvrei()
{
    cout<<"A- Afiseaza alfabetic\nB- Afiseaza buget dupa medie\nT - Afiseaza taxa dupa medie\nR - Afiseaza cei respinsi\n\n";
    char caz;
    cin>>caz;
    switch (caz) {
      case 'A':
        sorteaza_datele();
        Afiseaza(0,i,'A');
        break;
      case 'B':
        sorteaza_medie();
        Afiseaza(0,i,'B');
        break;
      case 'T':
        sorteaza_medie();
        Afiseaza(0,i,'T');
        break;
      case 'R':
        sorteaza_medie();
        Afiseaza(0,i,'R');
        break;
    }
}

int main()
{
    int n;
    cin>>n;
    while(n--)
    {
        int a,b,c,d;
        string n;
        cin>>a>>n>>b>>c>>d;
        adauga_elev(a,n,b,c,d);
    }
    Calculeaza_buget();
    Afiseaza_cumvrei();
    return 0;
}
