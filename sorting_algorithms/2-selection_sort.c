#include "sort.h"

/**
 * selection_sort - sorts an array of integers in
 * ascending order using the
 * Selection sort algorithm
 * @array: array to be sorted
 * @size: size of array
 *
 */
void selection_sort(int *array, size_t size)
{
	int temp = 0;
	size_t i = 0, j = 0, mpos;

	if (size < 2)
		return;
	for (i = 0; i < (size - 1); i++)
	{
		mpos = i;
		for (j = (i + 1); j < size; j++)
		{
			if (array[j] < array[mpos])
			{
				mpos = j;
			}
		}
		if (mpos != i)
		{
			temp = array[i];
			array[i] = array[mpos];
			array[mpos] = temp;
			print_array(array, size);
		}
	}
}
