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
    # There's nothing to return if there aren't two weights
    if len(weights) < 2:
        return None
    # Insert all weights below the limit into HT w/ key of weight & value of index
    for (i, w) in enumerate(weights):
        if i <= limit:
            hash_table_insert(ht, w, i)
    # For each weight, see if difference from limit exists in HT
    for (i1, w1) in enumerate(weights):
        w2 = limit - w1
        i2 = hash_table_retrieve(ht, w2)
        # If that weight exists...
        if i2 is not None:
            # Order indicies from smallest to largest and return
            return (i1, i2) if i1 > i2 else (i2, i1)
    # If you're here, then no matching pair was found
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
