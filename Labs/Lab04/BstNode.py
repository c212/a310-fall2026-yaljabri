class BstNode:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)
    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle
        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

# Reminder: this code will be given but you need to predict outcomes like below.
# 
# ================== RESTART: /Users/dgerman/Desktop/BstNode.py ==================
# a = BstNode(3)
# a.left = BstNode(5)
# a.left.right = BstNode(1)
# a.display()
#  _3
# /  
# 5  
#  \ 
#  1 
# b = BstNode(7)
# b.left = BstNode(4)
# a.right = b
# a.display()
#  _3_ 
# /   \
# 5   7
#  \ / 
#  1 4 
# b = BstNode(2)
# b.right = a.right
# a.right = b
# a.display()
#  _3   
# /  \  
# 5  2_ 
#  \   \
#  1   7
#     / 
#     4 
# a.right.left = BstNode(6)
# a.display()
#  _3_   
# /   \  
# 5   2_ 
#  \ /  \
#  1 6  7
#      / 
#      4 
# a.right.left.left = BstNode(8)
# a.display()
#  _3__   
# /    \  
# 5    2_ 
#  \  /  \
#  1  6  7
#    /  / 
#    8  4 
# a.right.left.right = BstNode(9)
# a.display()
#  _3___   
# /     \  
# 5    _2_ 
#  \  /   \
#  1  6   7
#    / \ / 
#    8 9 4 
# 

