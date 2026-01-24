#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x,y,n,p; // p indexat de la 1
    scanf("%d %d %d %d",&x,&y,&p,&n);
    int j=n-1;
    for(int i=p-1;i>=p-n;i--){
        int maskx=1<<i;
        int masky=1<<j;
        printf("%d\n",i);
        printf("x= %d y =%d \n",x,y);
        printf("x|mask = %d y|mask =%d \n",x|maskx,y|masky);
        if((x|maskx)==x /* sau (x & maskx) != 0 */){ // bitul din x este 1
            if((y|masky)!=y /* sau (y & masky) == 0 */){ // bitul de copiat din y este 0
                x=x^maskx; // dam toggle la bit deci din 1 devine 0 ca bitul din y
            }
            else
            if((y|masky)!=y){ // bitul de copiat din y este 1 ca si in x deci nu avem ceva de facut
                ///nimic
            }
        }
        else
        if((x|maskx)!=x  /* sau (x & maskx) == 0 */){ // bitul din x este 0
            if((y|masky)==y /* sau (y & masky) != 0 */){ // bitul de copiat din y este 1
                x=x^maskx; // dam toggle la bit deci din 0 devine 1 ca la bitul din y
            }
            else
            if((y|masky)==y){ // bitul de copiat din y este 0 ca si in x deci nu avem ceva de facut
                ///nimic
            }
        }
        j--; //schimbam pozitia pentru mask la y
    }
    printf("%d",x);
    return 0;
}
