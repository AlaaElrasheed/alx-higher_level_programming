#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted list
 * @head: head of list
 * @number: number to be inserted
 *
 * return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head, *new = malloc(sizeof(listint_t));

	if (new == NULL || head == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!tmp || new->n < tmp->n)
	{
		new->next = tmp;
		*head = new;
		return (*head);
	}
	while (tmp)
	{
		if (!tmp->next || new->n < tmp->next->n)
		{
			new->next = tmp->next;
			tmp->next = new;
			return (tmp);
		}
		tmp = tmp->next;
	}
	return (NULL);
}
