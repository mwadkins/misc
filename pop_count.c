#include <stdlib.h>
#include <iostream>

using namespace std;

unsigned pop_count (unsigned x) {
unsigned c = 0;
	while (x) {
	  if (x&1) {
 	    c++;
	  }
	  x >>=1;
   }
return c;
}

int main () {
  unsigned pc = pop_count(6);
  cout << pc << endl;
}
