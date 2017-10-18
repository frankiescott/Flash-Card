class Node():
    def __init__(self, q, a):
        self.question = q
        self.answer = a
        self.next = None
        self.score = 0
        self.hidden = False

class QList():
    first = None
    last = None
    size = 0
    def __init__(self):
        with open(".\\questions.txt", "r") as filestream:
            for line in filestream:
                currentline = line.rstrip('\n').split(",")
                self.add(currentline[0], currentline[1])
    def iter(self):
        return QListIterator(self.first)

    def allhidden(self):
        allhidden = True
        if self.first.hidden is False:
            return False
        else:
            n = self.first.next
            while n is not self.first:
                if n.hidden is False:
                    return False
                else:
                    n = n.next
        return True

    def reset(self):
        self.first.hidden = False
        self.first.score = 0
        n = self.first.next
        while n is not self.first:
            n.hidden = False
            n.score = 0
            n = n.next

    def add(self, q, a):
        n = Node(q, a)
        if self.first is None:
            self.first = n
            self.last = n

        n.next = self.first
        self.last.next = n
        self.last = n

    def getFirst(self):
        return self.first

class QListIterator():
    def __init__(self, node):
        self.n = node

    def next(self):
        cur = self.n
        while True:
            self.n = self.n.next
            if self.n.hidden is True:
                continue
            else:
                break
        return cur
