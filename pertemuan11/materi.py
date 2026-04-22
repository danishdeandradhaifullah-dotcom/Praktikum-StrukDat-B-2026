#ARRAY APPROACH
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,element):
        self.queue.append(element)

    def isEmpty(self):
        return len(self.queue) == 0
    
    def deQueue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]
    
myQueue = Queue()
myQueue.enqueue("A")
myQueue.enqueue("B")
myQueue.enqueue("C")
print("Before dequeue")
print(myQueue.queue)
print(myQueue.peek())
print(myQueue.isEmpty())
print(myQueue.size())
print("\nAfter dequeue")
dequeued = myQueue.deQueue()
print(dequeued)
print(myQueue.queue)
print(myQueue.peek())
print(myQueue.isEmpty())
print(myQueue.size())
print("\nAfter dequeue")

#AS LINKED LIST
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self,element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1
    
    def isEmpty(self):
        return self.length == 0
    
    def deQueue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear is None
        return temp.data
    
    def size(self):
        return self.length
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data
    
    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print()

myLinkedQueue = LinkedQueue()

myLinkedQueue.enqueue('A')
myLinkedQueue.enqueue('B')
myLinkedQueue.enqueue('C')

print("Queue: ", end="")
myLinkedQueue.printQueue()
print("Peek: ", myLinkedQueue.peek())
print("Dequeue: ", myLinkedQueue.deQueue())
print("Queue after Dequeue: ", end="")
myLinkedQueue.printQueue()
print("isEmpty: ", myLinkedQueue.isEmpty())
print("Size: ", myLinkedQueue.size())