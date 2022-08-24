#include "lists.h"

/**
 * insert_node - function that inserts a number into a sorted
 *	singly-linked list
 * @head: ptr to the head of the linked list
 * @number: the int to insert
 * Return: NULL if the function fails
 *Otherwise, a ptr to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{

		new->next = node;
		*head = new;

		return (new);
	}

	while (node && node->next && node->next->n < number)

	node = node->next;
	new->next = node->next;
	node->next = new;

	return (new);

}
