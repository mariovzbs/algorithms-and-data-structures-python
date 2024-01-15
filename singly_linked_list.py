class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
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
        current.next = new_node

    def delete_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head == self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


def main():
    llist = LinkedList()
    llist.append(10)
    llist.append(20)
    llist.append(30)
    llist.insert_at_beginning(5)
    llist.insert_at_position(25, 2)
    llist.delete_by_value(20)
    llist.display()
    print("Length:", llist.length())


main()
