class Node:
    def __init__(self, nazwisko, ocena):
        self.nazwisko = nazwisko
        self.ocena = ocena
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.ocena) + self.nazwisko


class DuodirectionalList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addBeg(self, nazwisko, ocena):
        if not self.head:
            n = Node(nazwisko, ocena)
            self.head = n
            self.tail = n
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            new_node = Node(nazwisko, ocena)
            new_node.previous = n
            n.next = new_node
            self.head = new_node

    def addEnd(self, nazwisko, ocena):
        if not self.tail:
            n = Node(nazwisko, ocena)
            self.tail = n
            self.head = n
        else:
            n = self.tail
            while n.previous is not None:
                n = n.previous
            new_node = Node(nazwisko, ocena)
            new_node.next = n
            n.previous = new_node
            self.tail = new_node

    def insert(self, nazwisko, ocena, n):
        it = self.head
        for i in range(n):
            it = it.previous

        new = Node(nazwisko, ocena)
        new.next = it.next
        new.previous = it
        it.next.previous = new
        it.next = new

    def delBeg(self):
        n = self.head
        n.previous.next = None
        self.head = n.previous
        del(n)

    def delEnd(self):
        n = self.tail
        n.next.previous = None
        self.tail = n.next
        del(n)

    def najwiecej(self):
        n = self.tail
        max = n.ocena
        prymus = n
        while n.next is not None:
            n = n.next
            if n.ocena > max:
                max = n.ocena
                prymus = n
        return prymus.nazwisko

    def printListBeg(self):
        n = self.head
        while n:
            print(n)
            n = n.previous

    def printListEnd(self):
        n = self.tail
        while n:
            print(n)
            n = n.next


ll = DuodirectionalList()

ll.addEnd("bab",14)
ll.addEnd("test",28888899384)
ll.addBeg("ufhierhg",2.34)
ll.addBeg("eufreufog",2348465434)
ll.insert("gdziejestes",298346, 2)
print(ll.najwiecej())
#ll.add(True)
#ll.add("test")

ll.printListBeg()
ll.printListEnd()


