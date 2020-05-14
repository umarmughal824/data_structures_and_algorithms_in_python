"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def length(self):
        total = 0
        if self.head:
            total += 1
            current = self.head
            while current.next:
                current = current.next
                total += 1
        return total

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        index = 0
        if self.head and position > 0:
            index = 1
            current = self.head
            while current.next:
                if index == position:
                    return current
                current = current.next
                index += 1
            # first and last element case
            if index == position:
                return current
            else:
                return current
        else:
            return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        # handle single element
        if position > 0:
            index = 0
            if self.head:
                index = 1
                current = self.head
                while current.next:
                    if index == position - 1:
                        next = current.next
                        current.next = new_element
                        new_element.next = next
                        break
                    current = current.next
                    index += 1
            return current
        else:
            pass

    def delete(self, value):
        """Delete the first node with a given value."""
        if self.head:
            current = self.head
            prev = None
            while current.next:
                if(current.value == value):
                    # remove the head
                    if self.head == current:
                        self.head = current.next
                    else:  # if the element is not head / tail
                        prev.next = current.next
                    del current
                    return
                prev = current
                current = current.next
            else:
                if self.head == current:
                    self.head = None
                else:  # remove the tail
                    prev.next = current.next
                del current


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value
