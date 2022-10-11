#include "sort.h"

/**
 * quick_sort - sorts an array of integers in ascending
 * order using the Quick sort algorithm
 * @array: array to be sorted
 * @size: size of array
 *
 */
void quick_sort(int *array, size_t size)
{
	int len;

	if (size < 2)
		return;
	len = (int) size;
	quick_sort_recursion(array, 0, len - 1, size);
}

/**
 * quick_sort_recursion - is a quick sort recurson
 * @array: array to be sorted
 * @low: lower bound of partition
 * @high: upper bound of partition
 * @size: size of the array
 *
 */
void quick_sort_recursion(int *array, int low, int high, size_t size)
{
	int pivot_index;

	if (low < high)
	{
		pivot_index = lomuto(array, low, high, size);
		quick_sort_recursion(array, low, pivot_index - 1, size);
		quick_sort_recursion(array, pivot_index + 1, high, size);
	}
}

/**
 * lomuto - implements lomuto partitioning of array
 * @array: array to partion and quick sort
 * @low: lower boind of partion
 * @high: upper bound of partition
 * @size: size of the array
 * Return: next pivot index
 */
int lomuto(int *array, int low, int high, size_t size)
{
	int i, j, temp, pivot;

	pivot = array[high];
	j = low;
	for (i = low; i < high; i++)
	{
		if (array[i] <= pivot)
		{
			if (array[i] != array[j])
			{
				temp = array[i];
				array[i] = array[j];
				array[j] = temp;
				print_array(array, size);
			}
			j++;
		}
	}
	if (array[j] != pivot)
	{
		temp = array[j];
		array[j] = pivot;
		array[high] = temp;
		print_array(array, size);
	}
	return (j);
}
