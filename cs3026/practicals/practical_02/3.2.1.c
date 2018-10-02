#include <stdio.h>
#include <string.h>

void hexdump(void *address, int length) {

  unsigned char * currentByte = address ;
  for ( int i = 0; i < length; i++) {
    printf("%02x ", currentByte[i]);
  }
  printf("\n");
}

void main() {
  char string[] = "Hello, World!\n";
  hexdump(&string, strlen(string) + 1);
}
