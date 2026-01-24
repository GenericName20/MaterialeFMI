#include <fstream>

using namespace std;

ifstream cin("test.in");
ofstream cout("test.out");

int const nmax = 1e5+1;

struct locuinta{
    string adresa;
    int suprafata;
    string tip_locuinta;
    int nr_camere;
    bool balcon;
    bool decomandat;
    string casa;
}v[nmax];

int main()
{
    string rez;
    int n,maresup=0;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        bool balc,tipap;
        int sup,cam;
        string ad,til,cas;
        cin>>ad>>sup>>til>>cam;
        v[i].adresa=ad;v[i].suprafata=sup;v[i].tip_locuinta=til;v[i].nr_camere=cam;
        v[i].balcon=false;v[i].decomandat=false;v[i].casa="";
        if(v[i].tip_locuinta=="garsoniera")
            cin>>v[i].balcon;
        if(v[i].tip_locuinta=="apartament")
            cin>>v[i].decomandat;
        if(v[i].tip_locuinta=="casa")
            cin>>v[i].casa;
    }
    for(int i=0;i<n;i++)
    {
        if(v[i].balcon==1 && v[i].suprafata>maresup)
        {
            maresup=v[i].suprafata;
            rez=v[i].adresa;
        }
        //cout<<v[i].adresa<<"\n"<<v[i].suprafata<<"\n"<<v[i].tip_locuinta<<" "<<'\n'<<v[i].balcon<<" "<<v[i].decomandat<<" "<<v[i].casa<<"\n\n";
    }
    cout<<rez;
    return 0;
}
