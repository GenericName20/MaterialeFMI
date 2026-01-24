#include <iostream>

using namespace std;

int v[10];

int main()
{
    int n;
    cin>>n;
    while(n!=0)
    {
        v[n%10]++;
        n/=10;
    }
    ///numarul mic
    int cnt,ti=0,i=1;
    while(v[i]==0)
    {
        i++;
    }
    cout<<i;
    ti=i;
    for(i=0;i<=9;i++)
    {
        if(i!=ti)
        {
            cnt=0;
            while(v[i]!=cnt)
            {
                cout<<i;
                cnt++;
            }
        }
        else
        if(i==ti)
        {
            cnt=1;
            while(v[i]>cnt)
            {
                cout<<i;
                cnt++;
            }
        }
    }
    cout<<'\n';
    // numarul mare
    for(int i=9;i>=0;i--)
    {
        cnt=0;
        while(v[i]!=cnt)
        {
            cout<<i;
            cnt++;
        }
    }
    return 0;
}