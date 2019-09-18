#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 *@head: linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 **/
int is_palindrome(listint_t **head)
{
	listint_t *p;
	int i, size = 0, j;
	int a[1024];

	if (head == NULL || *head == NULL)
		return (1);
	p = *head;
	while (p->next != NULL)
	{
		a[size] = p->n;
		size++;
		p = p->next;
	}
	j = size;
	for (i = 0; i <= size / 2; i++, j--)
		if (a[i] != a[j])
			return (0);
	return (1);
}
