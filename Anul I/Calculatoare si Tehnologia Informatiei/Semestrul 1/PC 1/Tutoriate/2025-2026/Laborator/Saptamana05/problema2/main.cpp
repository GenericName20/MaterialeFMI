#include <iostream>
using namespace std;

int main()
{
    long long a,b;
    char c;
    cin>>a>>c>>b;
    if(c=='+'){
        cout<<a+b;
        return 0;
    }
    if(c=='-'){
        cout<<a-b;
        return 0;
    }
    if(c=='*'){
        cout<<a*b;
        return 0;
    }
    if(c=='/'){
        if(b!=0)
            cout<<a/b;
        else
            cout<<"Nu poti imparti la 0";
        return 0;
    }
    if(c=='%'){
        if(b!=0)
            cout<<a%b;
        else
            cout<<"Nu poti face modul de 0";
        return 0;
    }
    cout<<"Operatorul nu este corect!";
    return 0;
}
