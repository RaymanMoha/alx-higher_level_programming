#include "sort.h"

/**
 * insertion_sort_list - sorts a doubly linked list
 * of integers in ascending order using the
 * Insertion sort algorithm
 * @list: doubly linked list
 *
 */
void insertion_sort_list(listint_t **list)
{
	listint_t *front = NULL, *back = NULL, *temp1 = NULL;

	front = (*list)->next;
	if (!list || !(*list) || (*list)->next == NULL)
		return;
	while (front != NULL)
	{
		temp1 = front->next;
		back = front->prev;
		while (back != NULL && back->n > front->n)
		{
			front->prev = back->prev;
			if (back->prev != NULL)
				front->prev->next = front;
			else
				*list = front;
			back->next = front->next;
			if (front->next != NULL)
				back->next->prev = back;
			back->prev = front;
			front->next = back;
			back = front->prev;
			print_list(*list);
		}
		front = temp1;
	}
}
