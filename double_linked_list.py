class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.tail:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.previous = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        new_node.previous = self.tail
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return
        elif position == self.length() - 1:
            self.insert_at_end(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if current is None:
                return
            current = current.next
        if current is None:
            return
        new_node.next = current.next
        new_node.previous = current
        current.next.previous = new_node
        current.next = new_node

    def delete_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            if self.head:
                self.head.previous = None
            else:
                self.tail = None
            return
        current = self.head
        while current:
            if current.data == data:
                if current.next:
                    current.next.previous = current.previous
                    current.previous.next = current.next
                    current.next = None
                    current.previous = None
                else:
                    self.tail = current.previous
                    self.tail.next = None
                    current.previous = None
                return
            current = current.next

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" -> ")
            current = current.previous
        print("None")

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


def main():
    dlist = DoubleLinkedList()
    dlist.append(10)
    dlist.append(20)
    dlist.append(30)
    dlist.insert_at_beginning(40)
    dlist.insert_at_position(50, 3)
    dlist.insert_at_position(60, 2)
    dlist.display_forward()
    dlist.delete_by_value(60)
    dlist.delete_by_value(50)
    dlist.display_forward()


main()
