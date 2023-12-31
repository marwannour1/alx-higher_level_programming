#include "lists.h"
#include <stdlib.h>

/*
 * insert_node - djfdf
 * @head: head
 * @number: number
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (!node || new_node->n < node->n)
	{
		new_node->next = node;
		*head = new_node;
		return (*head);
	}
	while (node->next != NULL && node->next->n < number)
	{
		node = node->next;
	}
	new_node->next = node->next;
	node->next = new_node;
	return (new_node);
}
