#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # Since HT is guaranteed to be at load 1, resize it for 0.5
    hash_table_resize(hashtable)
    # Insert tickets w/ source as key and destination as value
    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)
    
    i = 0
    # Retrieve first ticket (source = "NONE")
    dest = hash_table_retrieve(hashtable, "NONE")
    while i < len(route):
        # Insert destination at index
        route[i] = dest
        # Increment index
        i += 1
        # Find the next destination
        dest = hash_table_retrieve(hashtable, dest)
    # Return final route
    return route
