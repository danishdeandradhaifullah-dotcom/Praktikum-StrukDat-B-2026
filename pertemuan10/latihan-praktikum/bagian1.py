#BAGIAN 1
class StackList:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self,url):
        self.items.append(url)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
print("\nBAGIAN 1")
myStack = StackList()

myStack.push("Youtube.com")
myStack.push("Google.com")
myStack.push("Netflix.com")

print(myStack.items)
print(myStack.is_empty())
print(myStack.pop())
print(myStack.peek())
print(myStack.size())

#BAGIAN 2
class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList():
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top == 0
    
    def push(self,url):
        newNode = Node(url)
        if self.count:
            newNode.next = self.top
        self.top = newNode
        self.count += 1

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        current_url = self.top
        self.top = self.top.next
        self.count -= 1
        return current_url.url
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.url
    
    def size(self):
        return self.count
    
    def traverseAndPrint(self):
        currentNode = self.top
        while currentNode:
            print(currentNode.url, end=" -> ")
            currentNode = currentNode.next
        print()

myLinkedStack = StackLinkedList()
myLinkedStack.push("Youtube.com")
myLinkedStack.push('Bing.com')
myLinkedStack.push('Yahoo.com')

print("\nBAGIAN 2")
print("LinkedList: ", end="")
myLinkedStack.traverseAndPrint()
print("Peek: ", myLinkedStack.peek())
print("Pop: ", myLinkedStack.pop())
print("LinkedList after Pop: ", end="")
myLinkedStack.traverseAndPrint()
print("isEmpty: ", myLinkedStack.is_empty())
print("Size: ", myLinkedStack.size()) 
