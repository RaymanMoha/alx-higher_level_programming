#include "sort.h"

/**
 * shell_sort - sorts an array of integers
 * in ascending order using the Shell sort
 * algorithm, using the Knuth sequence
 * @array: array to be sorted
 * @size: length of array
 *
 */
void shell_sort(int *array, size_t size)
{
	size_t h, n;

	if (size < 2)
		return;
	n = 1;
	while (n <= size)
	{
		n = (n * 3) + 1;
	}
	h = n / 3;
	knuth(array, size, h);
}

/**
 * knuth - uses knuth sequence to sort
 * @array: array
 * @size: size of array
 * @h: last gap sequence for array
 *
 */
void knuth(int *array, size_t size, size_t h)
{
	size_t gap = h, i, j, temp, front, back;

	for (i = gap; i > 0; i /= 3)
	{
		for (j = i; j < size; j++)
		{
			front = j;
			back = j - i;
			while (front >= (0 + i))
			{
				if (array[front] < array[back])
				{
					temp = array[back];
					array[back] = array[front];
					array[front] = temp;
				}
				back = back - i;
				front = front - i;
			}
		}
		print_array(array, size);
	}
}
