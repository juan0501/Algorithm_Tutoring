#include <stdio.h>
#include <stdlib.h>
#define SIZE 10

typedef struct 
{
	int key;
} element;

typedef struct linkedlist {
	element item;
	struct linkedlist *link;
} list;

list *hashTable[SIZE];

int hash_function(int key) {
	return key % SIZE;
}

void hash_chain_add(element item, list *ht[]) {
	int hashValue = hash_function(item.key);
	list *ptr;
	list *nodeBefore = NULL, *node = ht[hashValue];
	for(; node; nodeBefore = node, node = node->link) {
		if(node->item.key == item.key){
			fprintf(stderr, "Error insert\n");
			return;
		}
	}
	ptr = (list*)malloc(sizeof(list));
	ptr->item = item;
	ptr->link = NULL;

	if(nodeBefore) nodeBefore->link = ptr;
	else ht[hashValue] = ptr;
}

void hash_chain_search(element item, list *ht[]) {
	list *node;
	int hashValue = hash_function(item.key);

	for(node = ht[hashValue]; node; node = node->link) {
		if(node->item.key == item.key) {
			fprintf(stderr, "%d is here\n", node->item.key);
			return;
		}
	}
	printf("There isn't %d\n", item.key);
}

void hash_chain_print(list *ht[]) {
	for(int i = 0; i < SIZE; i++) {
		printf("[%d]-> ", i);
		for(list *node = ht[i]; node; node = node->link) {
			printf("%3d -> ", node->item.key);
		}
		printf("\n");
	}
}

int main() {
	element e;
	for(int i = 0; i < SIZE*SIZE; i++) {
		e.key = i;
		hash_chain_add(e, hashTable);
	}

	hash_chain_print(hashTable);

	/*
	for(int i = 0; i < SIZE; i++) {
		e.key = i;
		hash_chain_search(e, hashTable);
	}
	*/

	return 0;
}

