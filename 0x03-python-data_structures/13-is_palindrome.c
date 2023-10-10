#include "lists.h"

/**
  * rec_palindrome - uses recursion to check palindrom
  * @head: head of list
  * @end: end of list
  * Return: 0 if not 1 if is
  */
int rec_palindrome(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (rec_palindrome(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

/**
  * is_palindrome - dhfhdf
  * @head: dfjdjf
  * Return: 0 if not 1 if is
  */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (rec_palindrome(head, *head));
}
