#include <iostream>

using namespace std;

int main(int argc,     // argument count
         char* argv[], // argument values
         char* envp[]) // environment variables
{
  int i = 0;
  while(envp[i] != NULL) // envp se termina cu NULL
  {
    cout << envp[i] << '\n';
    i++;
  }
  
  return 0;
}
