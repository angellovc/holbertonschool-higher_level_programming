#include "lists.h"
#include <stdio.h>
/**
 *insert_node - insert a node into a linked list according to digits order
 *@head: head of the linked list
 *@number: new number
 *Return: null if its fail, pointer to a new node if it success
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp;

	head[1] = head[0];
	while (head[1] != '\0')
	{
		if (head[1]->next == '\0' || number <= head[1]->next->n)
		{
			new = malloc(sizeof(listint_t));
			if (new == '\0')
				return ('\0');
			new->n = number;
			if (head[1]->next == '\0' && number < head[1]->n)
			{
				tmp = head[1];
				head[0] = new;
				new->next = tmp;
			}
			else
			{
				tmp = head[1]->next;
				head[1]->next = new;
				new->next = tmp;
			}
			break;
		}
		head[1] = head[1]->next;
	}
	return (new);
}
