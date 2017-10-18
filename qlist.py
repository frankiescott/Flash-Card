class Node():
    def __init__(self, q, a):
        self.question = q
        self.answer = a
        self.next = None
        self.score = 0

class QList():
    first = None
    last = None
    size = 0
    def __init__(self):
        with open(".\\questions.txt", "r") as filestream:
            for line in filestream:
                currentline = line.rstrip('\n').split(",")
                self.add(currentline[0], currentline[1])

    def add(self, q, a):
        n = Node(q, a)
        if self.first is None:
            self.first = n
            self.last = n

        n.next = self.first
        self.last.next = n
        self.last = n

    def delete(self, n):
        if self.first is self.last:
            print("same")
            return True
        if n is self.first:
            self.last.next = self.first.next
            self.first = self.first.next
            return False
        else:
            i = self.first
            while i.next is not None:
                if i.next is n:
                    if n is self.last:
                        self.last = i
                    i.next = n.next
                    return False
                else:
                    i = i.next

    def getFirst(self):
        return self.first
