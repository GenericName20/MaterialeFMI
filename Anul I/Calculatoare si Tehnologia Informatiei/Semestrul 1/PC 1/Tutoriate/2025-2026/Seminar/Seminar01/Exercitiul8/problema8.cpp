#include <iostream>
#include <cmath>

using namespace std;
#define mare 1005

int v[mare];

int main()
{
    int n;
    cin>>n;
    v[0]=1;
    v[1]=1;
    for(int i=2;i<=n;i++)
    {
        v[i]=v[i-1]+v[i-2];
    }
    cout<<v[n];
    return 0;
}