#include <fstream>

using namespace std;
ifstream in("test.in");
ofstream out("test.out");

const int nmax=1e2+1;

long long a[nmax],b[nmax],r[nmax];

int main()
{
    int n,m;
    in>>n>>m;
    for(int i=1;i<=n;i++){
        char c;
        int x,y;
        in>>x>>c>>c>>y;
        a[y]=x;
    }
    for(int i=1;i<=m;i++){
        char c;
        int x,y;
        in>>x>>c>>c>>y;
        b[y]=x;
    }
    for(int i=0;i<=50;i++){
        for(int j=0;j<=50;j++){
            long long exp=i+j, coef=a[i]*b[j];
            r[exp]+=coef;
        }
    }
    for(int i=100;i>=0;i--){
        if(r[i]!=0)
            out<<r[i]<<"x^"<<i;
        if(i!=0 && r[i-1]>0)
            out<<"+";
    }
    return 0;
}
