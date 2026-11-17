from s001 import Given
import random


class Heap(Given):

    def __init__(self, key):
        super().__init__(key)

    def size(self):
        if self.left == None and self.right == None:
            return 1
        elif self.left == None:
            return 1 + self.right.size()
        elif self.right == None:
            return 1 + self.left.size()
        else:
            return 1 + self.right.size() + self.left.size()

    def insert(self, value):
        path = "{0:b}".format(self.size() + 1)
        self.helper(path[1:], value)
        self.clean()

    def helper(self, path, value):
        if path == "1":
            self.right = Heap(value)

        elif path == "0":
            self.left = Heap(value)

        else:
            nextStep = path[0]

            if nextStep == '0':
                self.left.helper(path[1:], value)
            else:
                self.right.helper(path[1:], value)

    def clean(self):
        if self.left != None:
            self.left.clean()

        if self.right != None:
            self.right.clean()

        if self.left == None and self.right == None:
            pass

        elif self.right == None:
            if self.key > self.left.key:
                (self.left.key, self.key) = (self.key, self.left.key)

        else:
            if self.key <= self.left.key and self.key <= self.right.key:
                pass

            elif self.left.key < self.right.key:
                (self.left.key, self.key) = (self.key, self.left.key)

            else:
                (self.right.key, self.key) = (self.key, self.right.key)

    def removeTop(self):
        path = "{0:b}".format(self.size())

        value = self.helperRemove(path[1:])
        self.key = value

        p = self
        last = path[-1]

        for c in path[1:-1]:
            if c == "0":
                p = p.left
            else:
                p = p.right

        if last == "0":
            p.left = None
        else:
            p.right = None

        self.cleanRemove()

        return self

    def helperRemove(self, path):
        if path == "1":
            return self.right.key

        elif path == "0":
            return self.left.key

        else:
            nextStep = path[0]

            if nextStep == '0':
                return self.left.helperRemove(path[1:])
            else:
                return self.right.helperRemove(path[1:])

    def cleanRemove(self):
        if self.left == None and self.right == None:
            pass

        elif self.right == None:
            if self.key > self.left.key:
                (self.left.key, self.key) = (self.key, self.left.key)

        else:
            if self.key <= self.left.key and self.key <= self.right.key:
                pass

            if self.left.key < self.right.key:
                (self.left.key, self.key) = (self.key, self.left.key)
                self.left.cleanRemove()

            else:
                (self.right.key, self.key) = (self.key, self.right.key)
                self.right.clean()


# These methods are outside the Heap class

def removeTop(heap):
    if heap == None:
        return None

    elif heap.left == heap.right == None:
        return None

    else:
        return heap.removeTop()


def display(heap):
    if heap == None:
        print(None)

    else:
        heap.display()


# Final testing using random values

b = Heap(random.randrange(-50, 50))
b.display()

for _ in [2, 3, 4, 5, 6, 7, 8, 9]:
    value = random.randrange(-50, 50)

    print("---------------( now inserting " + str(value) + " )--")

    b.insert(value)
    b.display()


for _ in range(12):
    print("Removing top of heap now ... heap becomes:")

    b = removeTop(b)
    display(b)