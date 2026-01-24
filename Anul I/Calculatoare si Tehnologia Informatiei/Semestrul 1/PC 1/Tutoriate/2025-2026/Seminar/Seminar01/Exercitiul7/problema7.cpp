#include <iostream>
#include <cmath>

using namespace std;

#define mare 1005

int n,p,val;

int v[mare];

int poz(int val1)
{
    for(int i=0;i<n;i++)
    {
        if(v[i]==val1)
            return i;
    }
    return -1;
}

void rotire(int p)
{
    int cnt=0;
    while(cnt<p)
    {
        for(int i=n-1;i>=0;i--)
        {
            v[i+1]=v[i];
        }
        v[0]=v[n];
        cnt++;
        /*for(int i=0;i<n;i++)
        {
            cout<<v[i]<<' ';
        }
        cout<<'\n';*/
    }
    for(int i=0;i<n;i++)
    {
        cout<<v[i]<<' ';
    }
    cout<<'\n';
}

int main()
{
    char C;
    cin>>n;
    cin>>C;
    for(int i=0;i<n;i++)
    {
        cin>>v[i];
    } 
    if(C=='a')
    {
        cin>>val;
        cout<<poz(val);
    }
    if(C=='b')
    {
        cin>>p;
        rotire(p);
    }
    return 0;
}