from BstNode import BstNode

def largestValue(bst):
    if bst.right == None:
        return bst.key
    else:
        return largestValue(bst.right)

class BST(BstNode):
    def __init__(self, name):
        super().__init__(name)
    def insert(self, value):
        if self.key == value:
            return
        elif self.key < value:
            if self.right == None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        else:
            if self.left == None:
                self.left = BST(value)
            else:
                self.left.insert(value)
    def find(self, value):
        if value == self.key:
            return True
        elif value > self.key:
            if self.right == None:
                return False
            else:
                return self.right.find(value)
        else:
            if self.left == None:
                return False
            else:
                return self.left.find(value)
    def remove(self, value): # assumes that value is in this tree somewhere 
        if self.key == value:
            if self.right == None:
                return self.left
            if self.left == None: # this will also help minimize 
                return self.right # changes due to recursive calls
            else:
                num = largestValue(self.left)
                self.key = num
                self.left = self.left.remove(num)
        elif self.key < value:
            self.right = self.right.remove(value)
        else:
            self.left = self.left.remove(value)
        return self # last step
            
            
a = BST(8)
for num in [1, 9, 7, 2, 6, 4, 5]:
    a.insert(num)
print("Consider this tree:")
a.display()
print("If I remove the root:")
a = a.remove(8)
a.display()

# Consider this tree:
#  _____8 
# /      \
# 1____  9
#      \  
#   ___7  
#  /      
#  2__    
#     \   
#    _6   
#   /     
#   4     
#    \    
#    5    
# If I remove the root:
#  ____7 
# /     \
# 1     9
#  \     
#  2__   
#     \  
#    _6  
#   /    
#   4    
#    \   
#    5   

nums = [25, 32, 8, 7, 12, 24, 41, 50, 36, 33, 38, 37, 15, 44, 29, 3, 4, 18, 23, 9, 11]

a = BST(nums[0]);
for elem in nums[1:]:
    a.insert(elem)
print("Here's a tree:")
a.display()

from random import shuffle

shuffle(nums)

for elem in nums:
    print("I will now remove: ", elem)
    a = a.remove(elem)
    if a is not None:
        a.display()
    else:
        print("The tree is now empty.")

# Here's a tree:
#     _____________25___               
#    /                  \              
#    8____             32_________     
#   /     \           /           \    
#  _7  __12_______   29      ____41___ 
# /   /           \         /         \
# 3   9_     ____24        36___     50
#  \    \   /             /     \   /  
#  4   11  15_           33    38  44  
#             \               /        
#            18_             37        
#               \                      
#              23                      
# I will now remove:  32
#     _____________25_               
#    /                \              
#    8____           29_________     
#   /     \                     \    
#  _7  __12_______         ____41___ 
# /   /           \       /         \
# 3   9_     ____24      36___     50
#  \    \   /           /     \   /  
#  4   11  15_         33    38  44  
#             \             /        
#            18_           37        
#               \                    
#              23                    
# I will now remove:  29
#     _____________25_________     
#    /                        \    
#    8____               ____41___ 
#   /     \             /         \
#  _7  __12_______     36___     50
# /   /           \   /     \   /  
# 3   9_     ____24  33    38  44  
#  \    \   /             /        
#  4   11  15_           37        
#             \                    
#            18_                   
#               \                  
#              23                  
# I will now remove:  18
#     ___________25_________     
#    /                      \    
#    8____             ____41___ 
#   /     \           /         \
#  _7  __12_____     36___     50
# /   /         \   /     \   /  
# 3   9_     __24  33    38  44  
#  \    \   /           /        
#  4   11  15_         37        
#             \                  
#            23                  
# I will now remove:  3
#    ___________25_________     
#   /                      \    
#   8____             ____41___ 
#  /     \           /         \
#  7  __12_____     36___     50
# /  /         \   /     \   /  
# 4  9_     __24  33    38  44  
#      \   /           /        
#     11  15_         37        
#            \                  
#           23                  
# I will now remove:  33
#    ___________25_______     
#   /                    \    
#   8____           ____41___ 
#  /     \         /         \
#  7  __12_____   36___     50
# /  /         \       \   /  
# 4  9_     __24      38  44  
#      \   /         /        
#     11  15_       37        
#            \                
#           23                
# I will now remove:  23
#    _________25_______     
#   /                  \    
#   8____         ____41___ 
#  /     \       /         \
#  7  __12___   36___     50
# /  /       \       \   /  
# 4  9_     24      38  44  
#      \   /       /        
#     11  15      37        
# I will now remove:  36
#    _________25_____     
#   /                \    
#   8____           41___ 
#  /     \         /     \
#  7  __12___     38    50
# /  /       \   /     /  
# 4  9_     24  37    44  
#      \   /              
#     11  15              
# I will now remove:  37
#    _________25___     
#   /              \    
#   8____         41___ 
#  /     \       /     \
#  7  __12___   38    50
# /  /       \       /  
# 4  9_     24      44  
#      \   /            
#     11  15            
# I will now remove:  44
#    _________25___   
#   /              \  
#   8____         41_ 
#  /     \       /   \
#  7  __12___   38  50
# /  /       \        
# 4  9_     24        
#      \   /          
#     11  15          
# I will now remove:  4
#   _________25___   
#  /              \  
#  8____         41_ 
# /     \       /   \
# 7  __12___   38  50
#   /       \        
#   9_     24        
#     \   /          
#    11  15          
# I will now remove:  15
#   _______25___   
#  /            \  
#  8____       41_ 
# /     \     /   \
# 7  __12_   38  50
#   /     \        
#   9_   24        
#     \            
#    11            
# I will now remove:  8
#  _______25___   
# /            \  
# 7____       41_ 
#      \     /   \
#   __12_   38  50
#  /     \        
#  9_   24        
#    \            
#   11            
# I will now remove:  38
#  _______25_   
# /          \  
# 7____     41_ 
#      \       \
#   __12_     50
#  /     \      
#  9_   24      
#    \          
#   11          
# I will now remove:  41
#  _______25_ 
# /          \
# 7____     50
#      \      
#   __12_     
#  /     \    
#  9_   24    
#    \        
#   11        
# I will now remove:  11
#  _____25_ 
# /        \
# 7__     50
#    \      
#   12_     
#  /   \    
#  9  24    
# I will now remove:  25
#  ___24_ 
# /      \
# 7__   50
#    \    
#   12    
#  /      
#  9      
# I will now remove:  7
#    24_ 
#   /   \
#  12  50
# /      
# 9      
# I will now remove:  24
#  12_ 
# /   \
# 9  50
# I will now remove:  12
# 9_ 
#   \
#  50
# I will now remove:  9
# 50
# I will now remove:  50
# The tree is now empty.
