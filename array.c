#include<stdio.h>
int main()
{
int n,k, sum = 0, c, array[100];
printf("Enter the number of integers : ");
scanf("%d %d", &k,&n);
for(c = 0; c < k; c++)
{
scanf("%d", &array[c]);
sum = sum + array[c];
}
printf("%d", sum);
return 0;
}
