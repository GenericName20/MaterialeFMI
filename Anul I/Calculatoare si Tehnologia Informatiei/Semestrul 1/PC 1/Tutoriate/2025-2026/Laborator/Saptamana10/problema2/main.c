#include <stdlib.h>
#include <string.h>

struct student
{
    int id;
    char *nume;
    char *prenume;
    double nota;
};

int checkid=10;
double newnota=2.0;
struct student student_nou;

void afisare (char *nume_fisier_binar, char *nume_fisier_text)
{
    FILE* fin = fopen(nume_fisier_binar,"rb");
    FILE* fout = fopen(nume_fisier_text,"w");

    struct student ins;
    while(fread(&ins.id, sizeof(int), 1, fin) == 1)
    {
        int nume_len;
        fread(&nume_len, sizeof(int), 1, fin);
        ins.nume = malloc(sizeof(char) * nume_len);
        fread(ins.nume, sizeof(char), nume_len, fin);

        int prenume_len;
        fread(&prenume_len, sizeof(int), 1, fin);
        ins.prenume = malloc(sizeof(char) * prenume_len);
        fread(ins.prenume, sizeof(char), prenume_len, fin);

        fread(&ins.nota, sizeof(double), 1, fin);

        fprintf(fout,"%d\n",ins.id);
        fprintf(fout,"%s\n",ins.nume);
        fprintf(fout,"%s\n",ins.prenume);
        fprintf(fout,"%lf\n",ins.nota);

        free(ins.nume);
        free(ins.prenume);
    }
    fclose(fout);
}

void creare(char *nume_fisier_binar)
{
    FILE* fout = fopen(nume_fisier_binar,"wb");

    struct student ins;
    int cont = scanf("%d",&ins.id);
    while(cont==1)
    {
        ins.nume = malloc(sizeof(char)*20);
        ins.prenume = malloc(sizeof(char)*20);

        scanf("%20s",ins.nume);
        scanf("%20s",ins.prenume);
        scanf("%lf\n",&ins.nota);

        ///salvare
        fwrite(&ins.id, sizeof(int), 1, fout);

        int nume_len = strlen(ins.nume) + 1;
        fwrite(&nume_len, sizeof(int), 1, fout);
        fwrite(ins.nume, sizeof(char), nume_len, fout);

        int prenume_len = strlen(ins.prenume) + 1;
        fwrite(&prenume_len, sizeof(int), 1, fout);
        fwrite(ins.prenume, sizeof(char), prenume_len, fout);

        fwrite(&ins.nota, sizeof(double), 1, fout);

        free(ins.nume);
        free(ins.prenume);
        cont = scanf("%d",&ins.id);
    }
    fclose(fout);
}

void modificare (char *nume_fisier_binar)
{
    FILE* fout = fopen(nume_fisier_binar,"r+b");

    struct student ins;
    while(fread(&ins.id, sizeof(int), 1, fout) == 1)
    {
        ///CITIRE
        int nume_len;
        fread(&nume_len, sizeof(int), 1, fout);
        ins.nume = malloc(sizeof(char) * nume_len);
        fread(ins.nume, sizeof(char), nume_len, fout);

        int prenume_len;
        fread(&prenume_len, sizeof(int), 1, fout);
        ins.prenume = malloc(sizeof(char) * prenume_len);
        fread(ins.prenume, sizeof(char), prenume_len, fout);
        fread(&ins.nota, sizeof(double), 1, fout);

        if(checkid==ins.id)
        {
            ins.nota=newnota;
            fseek(fout, -(sizeof(int) + sizeof(int) + nume_len + sizeof(int) + prenume_len + sizeof(double)), SEEK_CUR);
        }
        ///AFISARE
        fwrite(&ins.id, sizeof(int), 1, fout);

        nume_len = strlen(ins.nume) + 1;
        fwrite(&nume_len, sizeof(int), 1, fout);
        fwrite(ins.nume, sizeof(char), nume_len, fout);

        prenume_len = strlen(ins.prenume) + 1;
        fwrite(&prenume_len, sizeof(int), 1, fout);
        fwrite(ins.prenume, sizeof(char), prenume_len, fout);

        fwrite(&ins.nota, sizeof(double), 1, fout);

        free(ins.nume);
        free(ins.prenume);
    }
    fclose(fout);
}

void adaugare (char *nume_fisier_binar)
{
    FILE* fout = fopen(nume_fisier_binar,"r+b");
    struct student ins;
    while(fread(&ins.id, sizeof(int), 1, fout) == 1)
    {
        ///CITIRE
        int nume_len;
        fread(&nume_len, sizeof(int), 1, fout);
        ins.nume = malloc(sizeof(char) * nume_len);
        fread(ins.nume, sizeof(char), nume_len, fout);

        int prenume_len;
        fread(&prenume_len, sizeof(int), 1, fout);
        ins.prenume = malloc(sizeof(char) * prenume_len);
        fread(ins.prenume, sizeof(char), prenume_len, fout);
        fread(&ins.nota, sizeof(double), 1, fout);

        free(ins.nume);
        free(ins.prenume);
    }

    fwrite(&student_nou.id, sizeof(int), 1, fout);

    int nume_len = strlen(student_nou.nume) + 1;
    fwrite(&nume_len, sizeof(int), 1, fout);
    fwrite(student_nou.nume, sizeof(char), nume_len, fout);

    int prenume_len = strlen(student_nou.prenume) + 1;
    fwrite(&prenume_len, sizeof(int), 1, fout);
    fwrite(student_nou.prenume, sizeof(char), prenume_len, fout);

    fwrite(&student_nou.nota, sizeof(double), 1, fout);

    fclose(fout);
}

int main()
{
    int n;
    student_nou.id=9;
    student_nou.nume="nume1";
    student_nou.prenume="prenume1";
    student_nou.nota=10.9;
    creare("open.bin");
    afisare("open.bin","close.txt");
    modificare("open.bin");
    afisare("open.bin","close1.txt");
    adaugare("open.bin");
    afisare("open.bin","close2.txt");
    return 0;
}

void adaugare (char *nume_fisier_binar)
{
    FILE* fout = fopen(nume_fisier_binar,"r+b");
    struct student ins;
    while(fread(&ins.id, sizeof(int), 1, fout) == 1)
    {
        ///CITIRE
        int nume_len;
        fread(&nume_len, sizeof(int), 1, fout);
        ins.nume = malloc(sizeof(char) * nume_len);
        fread(ins.nume, sizeof(char), nume_len, fout);

        int prenume_len;
        fread(&prenume_len, sizeof(int), 1, fout);
        ins.prenume = malloc(sizeof(char) * prenume_len);
        fread(ins.prenume, sizeof(char), prenume_len, fout);
        fread(&ins.nota, sizeof(double), 1, fout);

        free(ins.nume);
        free(ins.prenume);
    }

    fwrite(&student_nou.id, sizeof(int), 1, fout);

    int nume_len = strlen(student_nou.nume) + 1;
    fwrite(&nume_len, sizeof(int), 1, fout);
    fwrite(student_nou.nume, sizeof(char), nume_len, fout);

    int prenume_len = strlen(student_nou.prenume) + 1;
    fwrite(&prenume_len, sizeof(int), 1, fout);
    fwrite(student_nou.prenume, sizeof(char), prenume_len, fout);

    fwrite(&student_nou.nota, sizeof(double), 1, fout);

    fclose(fout);
}

int main()
{
    int n;
    student_nou.id=9;
    student_nou.nume="nume1";
    student_nou.prenume="prenume1";
    student_nou.nota=10.9;
    creare("open.bin");
    afisare("open.bin","close.txt");
    modificare("open.bin");
    afisare("open.bin","close1.txt");
    adaugare("open.bin");
    afisare("open.bin","close2.txt");
    return 0;
}
