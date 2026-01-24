#include <iostream>
using namespace std;

int a[105][105], b[105][105];

int main() {
    int n;
    cin>>n;
    for(int i=1;i<=n;i++)
        for (int j=1;j<=n;j++)
            cin>>a[i][j];
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
            b[j][n-i+1]=a[i][j];
    for(int i=1;i<=n;i++) {
        for (int j=1;j<=n;j++)
            cout<<b[i][j]<<" ";
        cout<<"\n";
    }
    return 0;
}
