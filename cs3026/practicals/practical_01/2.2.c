#include <stdio.h>

void swap(int *a, int *b)
{
  int temp = *a;
  *a = *b;
  *b = temp;
}

int main ( int argc, char ** argv )
{
  int first = 10;
  int second = 20;

  swap(&first, &second);
  printf("first: %d, second: %d\n", first, second);
}

