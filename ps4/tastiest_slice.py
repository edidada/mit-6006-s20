from Set_AVL_Tree import BST_Node, Set_AVL_Tree
#######################################
# DO NOT REMOVE THIS IMPORT STATEMENT #
# DO NOT MODIFY IMPORTED CODE         #
#######################################

class Key_Val_Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self): 
        return "%s,%s" % (self.key, self.val)

class Part_B_Node(BST_Node):
    def subtree_update(A):
        super().subtree_update()
        left_sum = A.left.total if A.left else 0
        right_sum = A.right.total if A.right else 0
        A.total = left_sum + A.item.val + right_sum
        choices = [(left_sum + A.item.val, A.item.key)]
        if A.left:
            choices.append((A.left.best, A.left.best_key))
        if A.right:
            choices.append((left_sum + A.item.val + A.right.best, A.right.best_key))
        A.best, A.best_key = max(choices, key=lambda pair: (pair[0], -pair[1]))
        #########################################
        # ADD ANY NEW SUBTREE AUGMENTATION HERE #
        #########################################

class Part_B_Tree(Set_AVL_Tree):
    def __init__(self): 
        super().__init__(Part_B_Node)

    def max_prefix(self):
        if self.root is None or self.root.best <= 0:
            return (0, 0)
        return self.root.best_key, self.root.best

def tastiest_slice(toppings):
    tree = Part_B_Tree()
    ordered = sorted(toppings)
    best_x = best_y = best_total = 0
    index = 0
    while index < len(ordered):
        x = ordered[index][0]
        while index < len(ordered) and ordered[index][0] == x:
            _, y, value = ordered[index]
            if tree.root:
                node = tree.root.subtree_find(y)
            else:
                node = None
            if node is None:
                tree.insert(Key_Val_Item(y, value))
            else:
                node.item.val += value
                node.maintain()
            index += 1
        y, total = tree.max_prefix()
        if total > best_total:
            best_x, best_y, best_total = x, y, total
    return best_x, best_y, best_total
