class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        newNode = Node(data)
        if self.head is None :
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode


    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


    def deletebyval(self, data):
        if self.head.data == data:
            self.head = self.head.next
        else:
            prev = self.head
            curr = prev.next
            while curr is not None:
                if curr.data == data and curr.next is not None:
                    prev.next = curr.next
                elif curr.data == data and curr.next is None:
                    self.tail = prev
                    self.tail.next = None
                    break
                if prev.next is not None:
                    prev = prev.next
                    curr = prev.next

    def deletebyindex(self,index):
        tempidx = 0
        temp = self.head
        if index == 0:
            self.head = temp.next
        else:
            prev = self.head
            curr = prev.next

            while curr is not None:
                tempidx += 1
                if tempidx == index and curr.next is not None:
                    prev.next = curr.next
                    break
                elif tempidx == index and curr.next is None:
                    self.tail = prev
                    self.tail.next = None
                    break
                elif curr == self.tail:
                    print("List Out Of Bound Exception")
                if prev.next is not None:
                    prev = prev.next
                    curr = curr.next

    def size(self):
        index = 1
        temp = self.head
        while temp.next is not None:
            index += 1
            temp = temp.next
        print(index)


def main():
    l1 = linkedList()
    l1.insert(1)
    l1.insert(2)
    l1.insert(5)
    l1.insert(7)
  #  l1.deletebyindex(3)
    l1.display()
    l1.size()

if __name__ == '__main__':
    main()







