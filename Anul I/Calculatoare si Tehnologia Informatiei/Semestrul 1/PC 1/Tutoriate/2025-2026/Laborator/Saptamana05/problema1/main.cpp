#include <iostream>

using namespace std;

int main()
{
    char C;
    cin>>C;
    if(C<97)
        C+=32;
    cout<<C;
    return 0;
}
