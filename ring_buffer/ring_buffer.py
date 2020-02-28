from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If not at maximum capacity, add item to the tail.
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        # If at maximum capacity, remove the current head (the oldest item in storage) and then add the new item to tail.
        elif self.storage.length == self.capacity:
            removed = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)

            if removed == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # Loop through, appending the values to list_buffer_contents
        while len(list_buffer_contents) < self.storage.length:

            list_buffer_contents.append(self.current.value)

            if self.current.next:
            # If there is a next, set self.current to be self.current.next
                self.current = self.current.next
            else:
                self.current = self.storage.head

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
