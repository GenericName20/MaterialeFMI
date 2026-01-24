#include <iostream>

using namespace std;

int a[105][105];

int v[1000005];

int primulfp(int n)
{
    for(int i=2;i<10005;i++)
    {
        if(v[i]==0 && n!=0 && n%i==0)
            return i;
    }
    return -1;
}

int  main()
{
    int n,m;
    cin>>n>>m;
    v[1]=1;
    for(int i=2;i<=10005;i++)
    {
        if(v[i]==0)
        {
            for(int j=i*2;j<=10005;j=j+i)
            {
                v[j]=1;
            }
        }
    }
    v[1]=0;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
        {
            a[i][j]=-1;
        }
    }
    int cnt=1,total=0,i=1,j=1,cnt2=0;
    while(total+1<n*m)
    {
        while(a[i][j+1]==-1)
        {
            if(v[cnt]==1 && cnt2==1 && cnt!=1)
            {
                a[i][j]=primulfp(cnt);
                cnt2=0;
                cnt++;
            }
            else
            if(v[cnt]==1 && cnt2==0)
            {
                a[i][j]=cnt;
                cnt2=1;
            }
            else
                a[i][j]=cnt++;
            j++;
            total++;
        }
        while(a[i+1][j]==-1)
        {
            if(v[cnt]==1 && cnt2==1 && cnt!=1)
            {
                a[i][j]=primulfp(cnt);
                cnt2=0;
                cnt++;
            }
            else
            if(v[cnt]==1 && cnt2==0)
            {
                a[i][j]=cnt;
                cnt2=1;
            }
            else
                a[i][j]=cnt++;
            i++;
            total++;
        }
        while(a[i][j-1]==-1)
        {
            if(v[cnt]==1 && cnt2==1 && cnt!=1)
            {
                a[i][j]=primulfp(cnt);
                cnt2=0;
                cnt++;
            }
            else
            if(v[cnt]==1 && cnt2==0)
            {
                a[i][j]=cnt;
                cnt2=1;
            }
            else
                a[i][j]=cnt++;
            j--;
            total++;
        }
        while(a[i-1][j]==-1)
        {
            if(v[cnt]==1 && cnt2==1 && cnt!=1)
            {
                a[i][j]=primulfp(cnt);
                cnt2=0;
                cnt++;
            }
            else
            if(v[cnt]==1 && cnt2==0)
            {
                a[i][j]=cnt;
                cnt2=1;
            }
            else
                a[i][j]=cnt++;
            i--;
            total++;
        }
    }
    if(v[cnt]==1 && cnt2==1)
    {
        a[i][j]=primulfp(cnt);
        cnt2=0;
    }
    else
    if(v[cnt]==1 && cnt2==0)
    {
        a[i][j]=cnt;
        cnt2=1;
    }
    else
        a[i][j]=cnt++;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
        {
            printf("%2d ",a[i][j]);
        }
        cout<<'\n';
    }
    return 0;
}