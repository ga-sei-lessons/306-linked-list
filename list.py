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

    def insert_end(self, data):
        """
        Instance method that inserts a new node using with the given data at the end of the list
        @param data The data value to insert at the end of the list.
        """
        new_node = Node(data)
        # if this is the first node in the list, set to be both head and tail
        if len(self) == 0:
            self.tail = new_node
            self.head = self.tail
        # otherwise set the current tail's next to be the new node and replace the tail
        else:
            # update the tail's next value for iteration
            self.tail.next = new_node
            # update the list's tail for future insertion
            self.tail = new_node

        self.size += 1

    def find(self, data): 
        """
        Instance method that searches the list for the given data and returns when the first instance of it is found.
        @param data The data to search the list for
        @return The node of data if it is found, None if it is not.
        """
        # iterate the list using a while loop
        current_node = self.head
        while current_node:
            # if we encounter the data we are looking for, return the new node immediately
            if current_node.data == data: 
                return current_node
            
            # move iteration forward
            current_node = current_node.next
        
        # if iteration stops, we need to return None (not found)
        return None

