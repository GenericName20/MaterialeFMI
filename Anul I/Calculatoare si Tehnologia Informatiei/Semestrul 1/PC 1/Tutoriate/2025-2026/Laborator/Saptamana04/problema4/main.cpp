#include <fstream>
#include <vector>

using namespace std;

ifstream in("test.in");
ofstream out("test.out");

struct date{
    unsigned short varsta:7;
    string nume;
    bool norma;
    string cnp;
}v[10];

struct au{
    unsigned short aux:7;
}ca;

int main()
{
    int n;
    in>>n;
    out<<sizeof(date)<<'\n';
    for(int i=0;i<n;i++)
    {
        unsigned short x;
        in>>x;
        v[i].varsta=x;
        in>>v[i].nume;
        in>>v[i].norma;
        in>>v[i].cnp;
        //out<<v[i].varsta.numar<<" "<<v[i].nume<<" "<<v[i].norma<<" "<<v[i].cnp<<'\n';
        ca.aux=x;
        ca.aux=(v[i].varsta<<2);
        if(v[i].varsta==ca.aux>>2 && v[i].cnp[0]=='5')
            out<<v[i].varsta<<'\n';
    }
    return 0;
}
