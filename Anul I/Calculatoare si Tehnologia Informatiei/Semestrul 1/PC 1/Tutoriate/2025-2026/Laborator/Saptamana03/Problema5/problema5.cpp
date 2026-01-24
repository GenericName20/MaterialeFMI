#include <iostream>

using namespace std;

int a[105][105];

int  main()
{
    int n,m,total=0;
    cin>>n>>m;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            cin>>a[i][j];
        }
    }
    int cnt=0,i=0,j=0;
    while(total<n*m)
    {
        while(j<m-cnt)
        {
            cout<<a[i][j]<<' ';
            total++;
            j++;
        }
        j--;
        i++;
        if(total>=n*m)break;
        while(i<n-cnt)
        {
            cout<<a[i][j]<<' ';
            total++;
            i++;
        }
        j--;
        i--;
        if(total>=n*m)break;
        while(j>=0+cnt)
        {
            cout<<a[i][j]<<' ';
            total++;
            j--;
        }
        i--;
        j++;
        cnt++;
        if(total>=n*m)break;
        while(i>=0+cnt)
        {
            cout<<a[i][j]<<' ';
            total++;
            i--;
        }
        j++;
        i++;
        if(total>=n*m)break;
    }
    return 0;
}