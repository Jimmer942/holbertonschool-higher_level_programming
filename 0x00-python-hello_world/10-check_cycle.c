#include "lists.h"
/**
 * check_cycle - function that finds the loop in a linked list.
 * @list: pointer to the first node.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	if (list)
	{
		listint_t e, c;

		for (c.n = 1, e.next = list->next; e.next; c.n++, list = c.next)
		{
			for (e.n = 0, c.next = list; list != e.next; e.n++)
				list = list->next;
			if (e.n != c.n)
				return (1);
			e.next = list->next;
		}
	}
	return (0);
}
