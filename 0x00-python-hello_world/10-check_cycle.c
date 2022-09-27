#include "lists.h"

/**

 * check_cycle - function that checks if a singly linked list has

 * a cycle in it

 * based on Floyd's cycle-finding algorithm

 * @list: pointer to the struct listint_t

 *

 * Return: 0 if there is no cycle, 1 if there is a cycle

 */

int check_cycle(listint_t *list)

{
	listint_t *slow = list, *fast = list;

	while (fast)
	{

		slow = slow->next;

		if (fast->next == NULL)
			break;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
}
	return (0);
}
