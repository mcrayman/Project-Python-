
class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

class BadLLQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        result = 'BadLLQueue (back to front): '
        temp = self.head
        while temp != None:
            result += str(temp.data) + ' '
            temp = temp.next
        return result

    def enqueue(self, new_data):
        # Add a new node to the head of the list
        # Start by creating a new Node object
        if self.size == 0:
            self.head = self.tail = Node(new_data, None)


        else:
            self.head = Node(new_data, self.head)


        self.size += 1

    def dequeue(self):
        # Remove and return the data at the front of the queue (tail of the
        #  list)
        if self.size == 0:
            return None
        else:
            if self.size == 1:
                temp = self.tail.data
                self.head = self.tail = None

                self.size -= 1
                return temp

            else:
                temp = self.tail.data
                curr = self.head
                while curr.next != self.tail:
                    curr = curr.next
                self.tail = curr
                self.tail.next = None

                self.size -= 1
                return temp


    def peek(self):
        # Return the data at the front of the queue (head of the list)
        if self.size > 0:
            return self.tail.data

if __name__ == '__main__':
    q = BadLLQueue()
    print(q)

    for i in range(6):
        q.enqueue(i)
        print(q)
    print()

    for i in range(q.size + 1):
        print('dequeue: ', q.dequeue())
        print(q)
    print()

    for i in range(1, 6):
        print(q)
        print(q.peek())
        q.enqueue(i)
