#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    index = 0

    for item in weights:
        weight_diff = limit - item
        existing_index = hash_table_retrieve(ht, item)

        if existing_index == 0 or existing_index:
            return (index, existing_index)
        hash_table_insert(ht, item, index)
        index += 1

    for item in weights:
        weight_diff = limit - item

        weight_index = hash_table_retrieve(ht, weight_diff)

        if weight_index is not None:
            current_index = hash_table_retrieve(ht, item)
            if current_index > weight_index:
                return (current_index, weight_index)
            else:
                return (weight_index, current_index)

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
