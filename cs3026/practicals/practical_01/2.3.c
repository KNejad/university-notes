#include <stdio.h>

#define BUFFER_SIZE 512

int main(int argc, char **argv )
{
  char buf [ BUFFER_SIZE + 1 ] ;
  int lines = 0 ;
  int words = 0 ;
  int chars = 0 ;
  int linelength = 0 ;
  char currentCharacter;

  while (!feof(stdin))
  {
    currentCharacter = getchar();
    chars++;

    if (currentCharacter == ' ')
    {
      words++;
    }

    if (currentCharacter == '\n')
    {
      lines++;
    }
  }
  printf("%d %d %d\n", chars, words, lines);
}
