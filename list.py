class Node:
    """
    A singly linked list node
    @param data = the data stored in this node
    @param next = the next node in the list
    """
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

# # node testing zone
# head = Node(1)
# # print(head)
# head.next = Node(2)
# # print(head, head.next)
# head.next.next = Node(3)
# # print(head, head.next, head.next.next, head.next.next.next)

# current_node = head # start iterating at the head
# while current_node:
#     print(current_node)
#     current_node = current_node.next

class LinkedList:
    """
    A singly linked list
    @param head The first node of the list
    @param tail The last node of the list
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        # makes our lists work with python's len() function
        return self.size

    def __str__(self):
        if len(self) == 0:
            return '[]'
        
        # always iterate starting at the head
        current_node = self.head
        string = str(current_node)
        while current_node.next:
            string += f" -> {current_node.next}"
            current_node = current_node.next
        
        return f"[ {string} ]"

    def insert_front(self, data):
        """
        Instance method that inserts given data at the beginning of the list.
        @param data The data to be inserted.
        """
        # is this the first item added to the list?
        new_node = Node(data)
        # if so, set new node to be both head and tail
        if len(self) == 0:
            self.head = new_node
            self.tail = self.head
        # otherwise, replace current head with new node
        else:
            # set the new node's tail to be the head
            new_node.next = self.head
            # replace head with new node
            self.head = new_node

        # increment the size of the list
        self.size += 1
