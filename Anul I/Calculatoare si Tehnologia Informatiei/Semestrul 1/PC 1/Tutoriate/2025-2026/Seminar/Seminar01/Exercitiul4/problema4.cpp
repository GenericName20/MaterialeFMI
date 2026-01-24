#include <iostream>
#include <cmath>

using namespace std;

int nrcif(long long n)
{
    int rez=0;
    while(n!=0)
    {
        rez++;
        n/=10;
    }
    return rez;
}

int main()
{
    long long n,ns,sum=0;
    cin>>n;
    ns=n;
    bool intrat=true;
    while(n!=ns || intrat==true)
    {
        intrat=false;
        int c=n%10;
        n=pow(10,nrcif(n))*c+n;
        n/=10;
        sum+=n;
    }
    cout<<sum;
    return 0;
}