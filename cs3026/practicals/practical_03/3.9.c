#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern char **environ;

int main()
{
  char buffer[80];

  while (1)
  {
    printf ("[myShell]> ");
    scanf ("%s", buffer);

    if (strcmp(buffer, "cls") == 0) {
      system("clear");
      continue;
    }

    if (strcmp(buffer, "dir") == 0) {
      char arg[80];
      scanf("%s", arg);
      strcat(buffer, " ");
      strcat(buffer, arg);
      system(buffer);
      continue;
    }

    if (strcmp(buffer, "environ") == 0) {
      char ** env = environ;
      while ( *env != NULL )
      {
        printf( "%s\n",*env );
        env++ ;
      }
      continue;
    }

    if (strcmp(buffer, "quit") == 0) exit(0);

    system(buffer);
  }
}
