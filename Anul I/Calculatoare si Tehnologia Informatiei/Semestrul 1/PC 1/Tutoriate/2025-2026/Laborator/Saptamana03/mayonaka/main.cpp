#include <bits/stdc++.h>

using namespace std;

ifstream in("mayonaka.in");
ofstream out("mayonaka.out");

const int mare=100005;

int n, m, rad;
int r[mare];

bool ver[mare];
int a[330][mare];

int main()
{
    in>>n>>m;
    rad=sqrt(n);
    int x,y,s,g;
    for(int i=1;i<=m;i++)
    {
        in>>x>>y>>s>>g;
        if(s>=rad)
        {
            for(int j=x;j<=y;j+=s)
            {
                r[j]+=g;
            }
        }
        else
        {
            int st=x;
            int dr=min(n+1,x+((y-x)/s)*s+s);
            ver[s]=1;
            a[s][st]+=g;
            a[s][dr]-=g;
        }
    }
    for(int i=1;i<=rad;i++)
    {
        if(ver[i]==1)
        {
            for(int j=1;j<=n;j++)
            {
                if(j-i>=1)
                {
                    a[i][j]+=a[i][j-i];
                }
                r[j]+=a[i][j];
            }
        }
    }
    for(int i=1;i<=n;i++)
    {
        out<<r[i]<<' ';
    }
    return 0;
}
