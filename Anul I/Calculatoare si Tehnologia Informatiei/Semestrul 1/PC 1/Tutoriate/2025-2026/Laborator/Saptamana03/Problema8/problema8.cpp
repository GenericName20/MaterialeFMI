#include <bits/stdc++.h>

using namespace std;

int a[17][17];

int b[17][17],c[17][17];

long long sum=0;

void afisare(int a[17][17],int size)
{
    for(int i=1;i<=size;i++)
    {
        for(int j=1;j<=size;j++)
        {
            cout<<a[i][j]<<' ';
        }
        cout<<'\n';
    }
    cout<<'\n';
}

long long det(int a[17][17],int size)
{
    if(size==1)
    {
        //afisare(a,1);
        return a[1][1];
    }
    else
    if(size==2)
    {
        //afisare(a,2);
        return a[1][1]*a[2][2]-a[1][2]*a[2][1];
    }
    else
    if(size==3)
    {
        //afisare(a,3);
        return a[1][1]*a[2][2]*a[3][3]+a[2][1]*a[3][2]*a[1][3]+a[3][1]*a[1][2]*a[2][3]-a[1][3]*a[2][2]*a[3][1]-a[2][3]*a[3][2]*a[1][1]-a[3][3]*a[1][2]*a[2][1];
    }
    else
    for(int i1=1;i1<=size;i1++)
    {
        for(int j1=i1+1;j1<=size;j1++)
        {
            for(int h1=j1+1;h1<=size;h1++)
            {
                /// DET B
                for(int i=1;i<=3;i++)
                {
                    b[1][i]=a[i1][i];
                }
                for(int i=1;i<=3;i++)
                {
                    b[2][i]=a[j1][i];
                }
                for(int i=1;i<=3;i++)
                {
                    b[3][i]=a[h1][i];
                }
                /// DET C
                int cnti=1,cntj=1;
                bool gasit=false;
                for(int i=1;i<=size;i++)
                {
                    for(int j=1;j<=size;j++)
                    {
                        if(i!=i1 && i!=j1 && i!=h1 && j>3)
                        {
                            c[cntj][cnti]=a[i][j];
                            cnti++;
                            gasit=true;
                        }
                    }
                    if(gasit==true)
                    {
                        cnti=1;
                        cntj++;
                        gasit=false;
                    }

                }
                // puterea -1
                int inm=-1,putere=0;
                putere+=1+2+3+i1+j1+h1;
                inm=pow(-1,putere);
                sum+=inm*det(b,3)*det(c,size-3);
            }
        }
    }
    return 0;
}

int  main()
{
    int n;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            cin>>a[i][j];
        }
    }
    det(a,n);
    cout<<sum;
    return 0;
}