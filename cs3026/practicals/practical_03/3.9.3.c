#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern char **environ;

int main()
{
  char buffer[80];
  while(1) {
    printf("> ");
    fgets(buffer, 80, stdin);
    char ** argv = strtok(buffer, " ");
    printf("%c", argv[0]);
  }

}
