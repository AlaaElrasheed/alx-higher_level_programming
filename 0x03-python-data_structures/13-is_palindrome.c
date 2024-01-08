#include "lists.h"

/**
 * reverse_listint - reverses a listint_t linked list.
 * @head: head to be reversed
 *
 * Return: pointer to the first node of the reversed list
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *current = NULL, *tmp = NULL;

	while ( head != NULL && *head != NULL)
	{
		tmp = (*head)->next;
		(*head)->next = current;
		current = *head;
		*head = tmp;
	}
	return current;
}


/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: list to be checked
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *reverse = NULL, *tmp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		tmp = slow->next;
		slow->next = reverse;
		reverse = slow;
		slow = tmp;
	}
	if (fast != NULL)
		slow = slow->next;
	while (reverse != NULL && slow != NULL)
	{
		if (reverse->n != slow->n)
			return (0);
		reverse = reverse->next;
		slow = slow->next;
	}
    return (1);
}
