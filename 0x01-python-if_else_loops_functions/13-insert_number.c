#include "lists.h"
#include <stdio.h>
/**
 *new_listint - make a new listint struct
 *@n: element of the new struct
 *Return: pointer to a new struct
 */
listint_t *new_listint(int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == '\0')
		return ('\0');
	new->n = 0;
	new->next = '\0';
	new->n = n;
	return (new);
}
/**
 *insert_node - insert a node into a linked list according to digits order
 *@head: head of the linked list
 *@number: new number
 *Return: null if its fail, pointer to a new node if it success
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = '\0', *node;

	if (head == '\0')
		return ('\0');
	if (head[0] == '\0')
	{
		new = malloc(sizeof(listint_t));
		if (new == '\0')
			return ('\0');
		new->n = number;
		head[0] = new;
		return (new);
	}
	node = head[0];
	if (node != '\0' && number <= node->n)
	{
		new = new_listint(number);
		if (new == '\0')
			return ('\0');
		new->next = node;
		head[0] = new;
		return ('\0');
	}
	else
		while (node->next != '\0' && number > node->next->n)
			node = node->next;
	new = new_listint(number);
	if (new == '\0')
		return ('\0');
	new->next = node->next;
	node->next = new;
	return (new);
}
