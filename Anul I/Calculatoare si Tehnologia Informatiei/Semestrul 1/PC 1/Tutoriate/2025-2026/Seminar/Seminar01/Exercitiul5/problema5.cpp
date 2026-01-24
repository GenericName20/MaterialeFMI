#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int a,b;
    cin>>a>>b;
    int caca= pow(a%10,b);
    cout<<caca%10<<'\n';
    cout<<pow(a,b);
    return 0;
}