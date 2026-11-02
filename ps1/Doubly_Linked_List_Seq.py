class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        node = Doubly_Linked_List_Node(x)
        node.next = self.head
        if self.head is None:
            self.tail = node
        else:
            self.head.prev = node
        self.head = node

    def insert_last(self, x):
        node = Doubly_Linked_List_Node(x)
        node.prev = self.tail
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def delete_first(self):
        if self.head is None:
            raise IndexError('delete from empty list')
        node = self.head
        self.head = node.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        node.next = None
        return node.item

    def delete_last(self):
        if self.tail is None:
            raise IndexError('delete from empty list')
        node = self.tail
        self.tail = node.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        node.prev = None
        return node.item

    def remove(self, x1, x2):
        before, after = x1.prev, x2.next
        if before is None:
            self.head = after
        else:
            before.next = after
        if after is None:
            self.tail = before
        else:
            after.prev = before
        x1.prev = None
        x2.next = None
        result = Doubly_Linked_List_Seq()
        result.head, result.tail = x1, x2
        return result

    def splice(self, x, L2):
        if L2 is self:
            raise ValueError('Cannot splice a list into itself')
        if L2.head is None:
            return
        after = x.next
        x.next = L2.head
        L2.head.prev = x
        L2.tail.next = after
        if after is None:
            self.tail = L2.tail
        else:
            after.prev = L2.tail
        L2.head = L2.tail = None
