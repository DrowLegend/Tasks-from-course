class Node:

    def __init__(self, value=None):
        self.value = value
        self.node = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, value):

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        tmp = self.head

        while tmp.node:
            tmp = tmp.node

        tmp.node = new_node

    def print_list(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.node

    def count(self):
        tmp = self.head
        count = 0

        while tmp is not None:
            count += 1
            tmp = tmp.node
        return count

    def insert(self, i, value):
        new_node = Node(value)

        index = 1
        tmp = self.head

        while tmp.node and index < i:
            index += 1
            tmp = tmp.node

        next_node = tmp.node
        tmp.node = new_node
        new_node.node = next_node

    def delete(self):
        tmp = self.head

        while tmp.node.node:
            tmp = tmp.node

        tmp.node = None

    def delete_at(self, index):
        i = 0

        tmp = self.head
        previous = self.head

        while tmp.node and i < index:
            if i < index - 1:
                previous = tmp.node
            i += 1
            tmp = tmp.node

        previous.node = tmp.node


l = LinkedList()
l.add(11)
l.add(21)
l.add(31)
l.add(41)
l.add(51)
l.add(61)
# l.insert(3, 45)

#l.delete()

l.print_list()

l.delete_at(3)

# print("Count is: %d" % l.count())