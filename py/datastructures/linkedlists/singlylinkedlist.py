class Node():
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def __str__(self):
        return self.__repr__()
        
    def __repr__(self):
        return str(self.val)
        

class LinkedList():
    def __init__(self):
        self.head = None
        self.last = None
            
    def __str__(self):
        return self.traverse()
            
    def __repr__(self):
        return self.traverse()
            
    def add(self, node):
        if not self.head:   
            self.head = node
        else:
            self.last.next = node
        self.last = node
            
    def insert(self, after, node):
        if not self.head:
            self.add(node)
        else:
            next = self.head
            while next:
                if next.val == after.val:
                    node.next = next.next
                    next.next = node
                    break
                next = next.next
            
    def remove(self, val):
        next = self.head
        if next and next.val == val:
            self.head = next.next
            self.head = None
            next = None
            return
            
        prev = None
        while next:
            if next.val == val:
                break
            prev = next
            next = next.next

        if next and not next.next:
            self.last = prev
            prev.next = None
            next = None
        elif next:
            prev.next = next.next
            next = None
            
    def traverse(self):
        repr = ''
        next = self.head
        while next:
            repr = repr + '{}'.format(next.val)
            next = next.next
            
        return repr
            
