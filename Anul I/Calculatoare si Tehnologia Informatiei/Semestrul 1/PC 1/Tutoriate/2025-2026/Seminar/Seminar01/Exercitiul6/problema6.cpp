#include <iostream>
#include <cmath>

using namespace std;

int a[1005][1005];

int vf[100005];

int main()
{
    int n;
    cin>>n;
    a[1][0]=1;
    for(int i=2;i<=1000;i++)
    {
        for(int j=0;j<=(i+1)/2;j++)
        {
            if(i%2==0)
            {
                if(j==0)
                {
                    a[i][j]=a[i-1][j]*2;    
                }
                else
                if(j==i/2)
                    a[i][j]=1;
                else
                    a[i][j]=a[i-1][j]+a[i-1][j-1];
            }
            if(i%2==1)
            {
                if(j==i/2)
                    a[i][j]=1;
                else
                    a[i][j]=a[i-1][j]+a[i-1][j+1];
            }
        }
    }
    int rez=0;
    bool gasit=false;
    for(int i=1;i<1000;i++)
    {
        for(int j=0;j<1000;j++)
        {
            if(vf[a[i][j]]==0 && a[i][j]!=0)
            {
                vf[a[i][j]]=1;
                rez++;
            }
            if(rez==n)
            {
                gasit=true;
                break;
            }
            //printf("%4d ",a[i][j]);
        }
        if(gasit==true)
            break;
        //cout<<'\n';
    }
    rez=0;
    for(int i=1;i<=100005;i++)
    {
        if(vf[i]==1)
            rez++;
        if(rez==n)
        {
            cout<<'\n'<<i;
            return 0;
        }
    }
    return 0;
}