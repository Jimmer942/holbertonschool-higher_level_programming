#include "lists.h"
/**
 * insert_node - function that adds a new node in order on a list.
 * @head: where to list begin.
 * @number: int to insert.
 * Return: the adress of new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *p, *before, *after;

	if (head == NULL || *head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	p = *head;
	if (p->n >= number)
	{
		new = add_nodeint_begin(head, number);
		return (new);
	}
	while (p->next != NULL)
	{
		if (p->n == number)
		{
			new->n = number;
			new->next = p->next;
			p->next = new;
			return (new);
		}
		before = p;
		after = before->next;
		if (before->n < number && after->n > number)
		{
			new->n = number;
			new->next = after;
			before->next = new;
			return (new);
		}
		p = p->next;
	}
	new = add_nodeint_end(head, number);
	return (new);
}
