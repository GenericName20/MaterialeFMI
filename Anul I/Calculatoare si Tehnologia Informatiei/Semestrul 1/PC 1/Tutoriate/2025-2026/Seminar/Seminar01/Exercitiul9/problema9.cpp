#include <iostream>
#include <cmath>

using namespace std;

#define mare 1005

struct nrcomplex{
    double a;
    double b;
}x1,x2;

nrcomplex inm(nrcomplex k,nrcomplex h)
{
    float x1=k.a,y1=k.b;
    float x2=h.a,y2=h.b;
    k.a=x1*x2-y1*y2;
    k.b=x1*y2 + x2*y1;
    return k;
}

int main()
{
    double a,b,c,delta=0,n;
    cin>>a>>b>>c>>n;
    delta = b*b - 4*a*c;
    if(delta<0)
    {
        x1.a=-b/(2*a);
        x1.b=-sqrt(-delta)/(2*a);
        x2.a=-b/(2*a);
        x2.b=+sqrt(-delta)/(2*a);

        nrcomplex x1s=x1,x2s=x2;
        for(int i=1;i<n;i++)
        {
            x1=inm(x1,x1s);
            x2=inm(x2,x2s);
        }
        if(x1.b+x2.b!=0)
            cout<<int(x1.a+x2.a)<<"+"<<int(x1.b+x2.b)<<"i";
        else
            cout<<int(x1.a+x2.a);
    }
    if(delta>=0)
    {
        x1.a=(-b-sqrt(delta))/(2*a);
        x2.a=(-b+sqrt(delta))/(2*a);
        int rez=pow(x1.a,n)+pow(x2.a,n);
        cout<<rez;
    }
    return 0;
}