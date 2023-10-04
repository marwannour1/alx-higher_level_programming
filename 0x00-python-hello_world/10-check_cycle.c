#include "lists.h"

/*
 * check_cycle - checks if there is an infinite loop in a single linked list
 * @list: pointer to the begining of the single linked list
 *
 * Return: 0 if no loop, 1 if there is a loop
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
