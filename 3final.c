#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i, *ptr, sum = 0;
    FILE *source;
    source = fopen("data.txt", "r");
    int numofnum;
    fscanf(source, "%d", &numofnum);
    int arrnum[numofnum];

    ptr = (int*) malloc(numofnum * sizeof(int));

    if(ptr == NULL)                     
    {
        printf("Error! File is empty");
        exit(0);
    }

    for(i = 1; i < (numofnum + 1); ++i)
    {
        fscanf(source, "%d,", ptr + i);
        sum += *(ptr + i);
    }
    FILE *dest;
    dest = fopen("result.txt", "w"); 
    fprintf(dest, "Sum of %d numbers inserted in data.txt is %d \n", numofnum, sum);
    printf("Sum of numbers is stored in result.txt\n");
    fclose(source);
    fclose(dest);
    free(ptr);

    return 0;
}
