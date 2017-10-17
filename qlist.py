class Node():
    def __init__(self, q, a):
        self.question = q
        self.answer = a
        self.next = None

class QList():
    first = None
    last = None

    def __init__(self):
        with open("questions.txt", "r") as filestream:
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

    def getFirst(self):
        return self.first
