#include "lists.h"
/**
 *check_cycle - check if a linked list has a cycle
 *@list: linked list
 *Return: 0 if don't, 1 has a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *bunny;
	listint_t *turtle;

	bunny = list;
	turtle = list;
	while(turtle && bunny && bunny->next)
	{
		turtle = turtle->next;
		bunny = bunny->next->next;
		if (bunny == turtle)
			return (1);
	}
	return (0);
}
