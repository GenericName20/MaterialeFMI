#include <iostream>
using namespace std;
int main(int argc, char* argv[])
{
    cout << "Am " << argc << " argumente\n";
    for(int i = 0; i < argc; i++)
    {
        cout << i << ": " << argv[i] << '\n';
    }
    return 0;
}