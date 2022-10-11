#include "sort.h"

/**
 * cocktail_sort_list - sorts a doubly linked list
 * of integers in ascending order using the
 * Cocktail shaker sort algorithm
 * @list: doubly linked list to be sorted
 *
 */
void cocktail_sort_list(listint_t **list)
{
	listint_t *curr = NULL, *nxt = NULL;
	int swapped = 0;

	if (!list || !(*list) || !(*list)->next)
		return;
	do {
		curr = *list;
		while (curr->next != NULL)
		{
			nxt = curr->next;
			if (curr->n > nxt->n)
			{
				curr = swap_right(list, curr, nxt);
				swapped = 1;
				print_list(*list);
			}
			else
			{
				curr = curr->next;
			}
		}
		if (swapped == 0)
			break;
		swapped = 0;
		while (curr->prev != NULL)
		{
			nxt = curr->prev;
			if (curr->n < nxt->n)
			{
				curr = swap_left(list, curr, nxt);
				swapped = 1;
				print_list(*list);
			}
			else
			{
				curr = curr->prev;
			}
		}
	} while (swapped);
}

/**
 * swap_right - do a bubble swap moving to the right of list
 * @list:doubly linked list
 * @curr: current node on list
 * @nxt: next node to the right of current node
 * Return: current node
 */
listint_t *swap_right(listint_t **list, listint_t *curr, listint_t *nxt)
{
	nxt->prev = curr->prev;
	curr->prev = nxt;
	if (nxt->prev != NULL)
		nxt->prev->next = nxt;
	else
		*list = nxt;
	curr->next = nxt->next;
	if (curr->next != NULL)
		curr->next->prev = curr;
	nxt->next = curr;
	return (curr);
}

/**
 * swap_left - do bubble sort while moving from right to left
 * of list
 * @list: doubly linked list
 * @curr: current node
 * @nxt: node to left of current node
 * Return: current node
 */
listint_t *swap_left(listint_t **list, listint_t *curr, listint_t *nxt)
{

	nxt->next = curr->next;
	curr->prev = nxt->prev;
	nxt->prev = curr;
	if (nxt->next != NULL)
		nxt->next->prev = nxt;
	if (curr->prev != NULL)
		curr->prev->next = curr;
	else
		*list = curr;
	curr->next = nxt;
	return (curr);
}
