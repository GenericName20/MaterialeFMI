#include <iostream>

using namespace std;

int v[10];

int main()
{
    double x,lx=-1,mare=0,zi1=0,zi2=0;
    int n;
    cin>>n;
    cin>>lx;
    for(int i=1;i<n;i++)
    {
        cin>>x;
        if(x-lx>mare)
        {
            mare=x-lx;
            zi2=i;
            zi1=i-1;
        }
        lx=x;
    }
    cout<<zi1+1<<" "<<zi2+1<<" "<<mare;
    return 0;
}