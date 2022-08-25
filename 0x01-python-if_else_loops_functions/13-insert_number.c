#include "lists.h"

/*
 * insert_node - inserts a new node in sorted linked list
 * @head: listint_t double pointer input
 * @number: int input
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *current, *prev;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;

	if ((*head) == NULL)
		*head = newnode;
	else
	{
		current = *head;
		prev = NULL;

		while (current != NULL)
		{
			if (current->n > number)
				break;
			prev = current;
			current = current->next;
		}
		if (prev == NULL)
			*head = newnode;
		else
			prev->next = newnode;
		newnode->next = current;
	}
	return (newnode);
}
