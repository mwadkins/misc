#include <stddef.h>
#include <stdlib.h>
#include <iostream>
#include <vector>


using namespace std;

struct range {
  unsigned start;
  unsigned end;
  range (int s, int e): start(s),end(e) {}
};

ostream& operator<< (ostream& stream, const range& r) {
  return stream<<hex<<r.start<<"-"<<r.end;
}

void print (vector<range*> ranges) {
  vector<range*>::iterator it;
  for (it=ranges.begin(); it<ranges.end(); it++) {
    cout << **it<< endl;
  }
}

bool overlap (vector<range*> ranges) {
  vector<range*>::iterator it;
  for (it=ranges.begin(); it<ranges.end(); it++) {
    vector<range*>::iterator it2;
    for (it2=ranges.begin(); it2<ranges.end(); it2++) {
      if ((*it)!=(*it2)) {
	//if start > jstart and end < jend
	if ( ( ((*it)->start >= (*it2)->start) &&
	       ((*it)->start <= (*it2)->end)) ||
	     // if end > jstart and end < jend
	     (((*it)->end >= (*it2)->start) &&
	      ((*it)->end <= (*it2)->end))) {
	  cout << "overlap: " << **it << ","<< **it2 << endl;
	  //return false;
	}
      }
    }
  }
  return true;
}


int main () {
  vector<range*> v;
  int n = 5;
  unsigned s=0x0;
  for (int i=0; i < n; i++) {
    range* r = new range (s,s+0xfff);
    v.push_back(r);
    s+= 0x1000;
  }
  range* r = new range (0x2000,0x4000);
  v.push_back(r);

  r=new range (0x3fff,0x3fff);
  v.push_back(r);

  r=new range (0x5000,0x7000);
  v.push_back(r);
  
  r=new range (0x6000,0x9fff);
  v.push_back(r);

  
  bool ret = overlap(v);
  print (v);
}




