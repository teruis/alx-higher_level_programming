#include "lists.h"

/* Reverses a linked list */
void reverse_list(listint_t **head)
{
	listint_t *before = NULL, *after = NULL;
	listint_t *node = *head;

	while (node)
	{
		after = node->next;
		node->next = before;
		before = node;
		node = after;
	}
	*head = before;
}

/* 
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Pointer to head node of list
 * Returns: 1 if palindrome, 0 if not
*/
int is_palindrome(listint_t **head) {

  listint_t *first_half_head = *head; 
  listint_t *second_half_head = NULL;

  // Find middle of list using fast/slow pointers
  listint_t *slow = *head;
  listint_t *fast = *head;

  while (fast != NULL && fast->next != NULL) {
    slow = slow->next;
    fast = fast->next->next;
  }

  // Reverse second half
  second_half_head = slow->next;
  reverse_list(&second_half_head);

  // Compare first and second half
  while (first_half_head != NULL && second_half_head != NULL) {
    
    if (first_half_head->n != second_half_head->n) {
      return 0; 
    }
      
    first_half_head = first_half_head->next;
    second_half_head = second_half_head->next;
  }

  return 1;
}
