from s001 import Given


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

            elif self.left.key > self.right.key:
                (self.right.key, self.key) = (self.key, self.right.key)

            else:
                pass


print("---------------", 100)

a = Heap(100)
a.display()

for i in range(99, 92, -1):
    print("--------------- insert ", i)
    a.insert(i)
    a.display()