#include <stdio.h>
#include <stdlib.h>

struct complex{
    float a,b;
    void (*citire)(struct complex *);
    void (*afisare)(struct complex );
};

FILE* fin=NULL;
FILE* fout=NULL;

struct complex suma(struct complex *x,struct complex *y){
    struct complex r=*x;
    r.a=x->a + y->a;
    r.b=x->b + y->b;
    return r;
};

struct complex inmultire(struct complex *x,struct complex *y){
    struct complex r=*x;
    r.a= x->a*y->a - x->b*y->b;
    r.b= x->b*y->a + x->a*y->b;
    return r;
};

void cit(struct complex *x){
    float a1,b1;
    fscanf(fin,"%f %f",&x->a,&x->b);
}

void afs(struct complex x){
    if(x.a!=0){
        fprintf(fout,"%f",x.a);
    }
    if(x.b!=0){
        if(x.b>0)
            fprintf(fout," +");
        else
            fprintf(fout," ");
        fprintf(fout,"%fi",x.b);
    }
    fprintf(fout,"\n");
}

struct complex calcul(struct complex *x,struct complex *y,struct complex (*operatie)(struct complex *,struct complex *)){
    struct complex r=*x;
    r = operatie(x,x);
    return operatie(&r,y);
}

int main()
{
    fin = fopen("text.in","r");
    fout = fopen("text.out","w");
    struct complex nr1,nr2,nr3,nr4;
    nr1.citire=cit;nr3.citire=cit;
    nr1.afisare=afs;nr3.afisare=afs;
    nr2.citire=cit;nr4.citire=cit;
    nr2.afisare=afs;nr4.afisare=afs;

    nr1.citire(&nr1);
    fprintf(fout,"X=");
    nr1.afisare(nr1);
    nr2.citire(&nr2);
    fprintf(fout,"Y=");
    nr2.afisare(nr2);

    nr3 = calcul(&nr1,&nr2,inmultire);
    nr4 = calcul(&nr1,&nr2,suma);
    fprintf(fout,"X^2*Y=");
    nr3.afisare(nr3);
    fprintf(fout,"2X+Y=");
    nr4.afisare(nr4);

    fclose(fin);
    fclose(fout);
    return 0;
}
