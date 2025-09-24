#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    char s[100];

    // Read a line of input (including spaces) until newline
    scanf("%[^\n]%*c", s);

    // Print the required output
    printf("Hello, World!\n");
    printf("%s\n", s);

    return 0;
}