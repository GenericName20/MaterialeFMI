#include <bits/stdc++.h>

using namespace std;

int a[17][17];

int  main()
{
    int n;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            a[i][j]=-1;
        }
    }
    if(n%2==1)
    {
        int cnt=0,i=1,j=n/2+1;
        while(cnt<n*n)
        {
            if(a[i][j]==-1)
            {
                a[i][j]=cnt+1;
                cnt++;
            }
            i--;
            j--;
            if(i==0)
                i=n;
            if(j==0)
                j=n;
            if(a[i][j]!=-1 && i<n-1 && j<n)
            {
                i+=2;
                j++;
            }
        }
    }
    else
    if(n%4==0)
    {
        int cnt=1;
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
            {
                a[i][j]=cnt;
                cnt++;
            }
        }
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
            {
                if((j%4>=2 && i%4<2) || (i%4>=2 && j%4<2))
                {
                    if(j>=i)
                        swap(a[i][j],a[n-i+1][n-j+1]);
                }
            }
        }
    }
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            printf("%3d ",a[i][j]);
        }
        cout<<'\n';
    }
    return 0;
    
}
