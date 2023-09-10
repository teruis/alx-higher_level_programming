#include "lists.h"

int is_palindrome(listint_t **head) {
  listint_t *slow = *head;
  listint_t *fast = *head;

  if (*head == NULL || (*head)->next == NULL) {
    return (1); 
  }

  while (fast != NULL && fast->next != NULL) {
    slow = slow->next;
    fast = fast->next->next;
  }

  listint_t *second_half = reverse(&slow);
  listint_t *first_half = *head;

  while (second_half != NULL) {
    if (first_half->n != second_half->n) {
      return (0);
    }
    first_half = first_half->next;
    second_half = second_half->next;
  }

  return (1);
}

listint_t* reverse(listint_t **head) {
  listint_t *prev = NULL;
  listint_t *current = *head;

  while (current != NULL) {
    listint_t *next = current->next;
    current->next = prev;
    prev = current;
    current = next;
  }

  *head = prev;
  return prev;
}
