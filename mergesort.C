#include <iostream>
#include <stdlib.h>
#include <stddef.h> //for null

using namespace std;

struct node {
  node* next;
  int data;

  node (int d) : next(NULL),data(d) {}
};


void printlist (node* head) {
  node* curr = head;
  while (curr != NULL) {
    cout << curr->data << " ";
    curr=curr->next;
  }
  cout << endl;
}

void divideInHalf (node* head,node** a, node** b) {
  node* fast;
  node* slow;

  if ((head == NULL) || (head->next==NULL)) {
    *a=head;
    *b=NULL;
    return;
  }

  slow=head;
  fast=head->next;
  
  //move fast by two and slow by one
  while (fast != NULL) {
    fast=fast->next;
    if (fast != NULL) {
      slow=slow->next;
      fast=fast->next;
    }
  }

  *a=head;
  *b=slow->next;
  //break the list
  slow->next=NULL;
		     
}

node* mergeSortedHalves (node* a, node* b) {
  node* head=NULL;
  node* curr;
  node* prev;
 
  while ((a!=NULL) || (b!=NULL)) {
    if (a==NULL) {
      curr=b;
      b=b->next;
    } else if (b==NULL) {
      curr=a;
      a=a->next;
    } else if (a->data<=b->data) {
      curr = a;
      a=a->next;
    } else {
      curr = b;
      b=b->next;
    }
    if (head==NULL) {
      head=curr;
    } else {
      prev->next=curr;
    }
    prev=curr;
  }
  return head;
}

void mergesort (node** headref) {
  node* head = *headref;
  node* a;
  node* b;

  //base case, 0 or 1 element
  if ((head==NULL) || (head->next==NULL)) {
    return;
  }
  divideInHalf(head,&a,&b);

  mergesort(&a);
  mergesort(&b);
  *headref=mergeSortedHalves(a,b);
}



int main () {
  node* head;
  node* prev;
  for (int i=0; i<10; i++) {
    int r=rand() % 100;
    cout<<"adding "<<r<<endl;
    node* n = new node(r);
    if (prev!=NULL){
      prev->next=n;
    } else {
      head=n;
    }
    prev=n;
  }
  printlist(head);
  mergesort(&head);
  printlist(head);
}


















 
