#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: list to be checked
 *
 * Return: 1 or 0
 */

int check_cycle(listint_t *list)
{
	listint_t *new = list, *tmp = list;

	while (tmp && tmp->next)
	{
		new = new->next;
		tmp = tmp->next->next;
		if (new == tmp)
			return (1);
	}
	return (0);
}
