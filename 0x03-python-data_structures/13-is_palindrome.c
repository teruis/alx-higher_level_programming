int is_palindrome(listint_t **head) {
    if (*head == NULL || (*head)->next == NULL)
        return 1;

    listint_t *slow_ptr = *head;
    listint_t *fast_ptr = *head;
    listint_t *prev = NULL;
    listint_t *temp;

    while (fast_ptr != NULL && fast_ptr->next != NULL) {
        fast_ptr = fast_ptr->next->next;

        temp = slow_ptr->next;
        slow_ptr->next = prev;
        prev = slow_ptr;
        slow_ptr = temp;
    }

    if (fast_ptr != NULL)
        slow_ptr = slow_ptr->next;

    while (slow_ptr != NULL) {
        if (prev->n != slow_ptr->n)
            return 0;

        prev = prev->next;
        slow_ptr = slow_ptr->next;
    }

    return 1;
}

