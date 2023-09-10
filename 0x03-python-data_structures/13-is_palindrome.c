#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int len_list(listint_t *head)
{
	int i = 0;
	listint_t *h = head;

	while (head != NULL)
	{
		h = h->next;
		i++;
	}
	return (i);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: singly linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	int a, i;
	listint_t *tmp = *head;
	int array;

	l = len_list(*head);
	array = malloc(sizeof(int) * l);

	if (array == NULL)
	        exit(-1);

	i = 0;
	while (temp != NULL)
	{
		array[i] = temp->n;
		temp = temp->next;
		i++;
	}

