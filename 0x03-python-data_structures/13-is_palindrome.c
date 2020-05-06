#include "lists.h"
/**
 *palindrome_rec - check a palindrome into a linked list
 *@tail: linked list tail
 *@head: linked list head
 *Return: pointer to a linked list in success, NULL in failure
 */
listint_t *palindrome_rec(listint_t *tail, listint_t *head)
{
	if (tail->next != '\0')
		head = palindrome_rec(tail->next, head);
	if (head != '\0')
	{
		if (head->next == '\0')
			return (tail);
		if (head->n == tail->n)
			return (head->next);
	}
	return ('\0');
}
/**
 *is_palindrome - find if a linked list is a palindrome
 *@head: linked list
 *Return: 0 is not a palindrome, 1 in success
 */
int is_palindrome(listint_t **head)
{
	if (head[0] == '\0')
		return (1);
	if (palindrome_rec(head[0], head[0]) == '\0')
		return (0);
	return (1);
}
