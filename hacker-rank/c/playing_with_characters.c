#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    char ch;
    char str[100];
    char sentence[100];

    // Read a single character
    scanf("%c", &ch);

    // Read a string (up to first whitespace)
    scanf("%s", str);

    // Consume the leftover newline from previous input
    scanf("\n");

    // Read a full line (sentence)
    scanf("%[^\n]", sentence);

    // Print the outputs
    printf("%c\n", ch);
    printf("%s\n", str);
    printf("%s\n", sentence);

    return 0;
}