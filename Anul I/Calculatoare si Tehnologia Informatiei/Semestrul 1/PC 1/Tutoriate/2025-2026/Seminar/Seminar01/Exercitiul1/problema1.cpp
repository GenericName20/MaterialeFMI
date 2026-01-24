#include <iostream>

using namespace std;

int main()
{
    int n,ma1=-1,ma2=-1;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        int x;
        cin>>x;
        if(x>ma1)
        {
            ma2=ma1;
            ma1=x;
        }
        if(x>ma2 && x<ma1)
        {
            ma2=x;
        }
    }
    if(ma1==-1 || ma2==-1)
    {
        cout<<"Imposibil";
    }
    else
    {
        cout<<ma1<<' '<<ma2;
    }
    return 0;
}