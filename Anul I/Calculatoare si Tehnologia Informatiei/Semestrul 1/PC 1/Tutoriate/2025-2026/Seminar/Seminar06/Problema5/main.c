#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct student{
    int medie;
    char nume[20];
};

int comp(const void *a, const void *b) {
	struct student *studentA = (struct student *)a;
	struct student *studentB = (struct student *)b;

	if(studentA->medie == studentB->medie) {
		return strcmp(studentA->nume, studentB->nume);
	}
	return studentA->medie - studentB->medie;
}

int main()
{
    FILE* fin = fopen("text.in","r");
    FILE* fout = fopen("text.out","w");

    int n;
    fscanf(fin,"%d",&n);
    struct student v[n];
    for(int i=0;i<n;i++){
        fscanf(fin,"%d %s",&v[i].medie,&v[i].nume);
    }
    qsort(v, n, sizeof(struct student), comp);
    for(int i=0;i<n;i++){
        fprintf(fout,"%d %s\n",v[i].medie,v[i].nume);
    }
    return 0;
}
