from joueur import Joueur

class Node:  
    def __init__(self, data = 0, next = None):
        self.data: Joueur = data
        self.next: Node = next
        
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        if self.next is None:
            return repr(self.data)
        return repr(self.data) + ' -> ' + repr(self.next)
    
    def set_next(self, next):
        self.next = next
        
    def get_next(self):
        return self.next
    
    def set_data(self, data):
        self.data = data
        
    def get_data(self):
        return self.data
   
class ListeChainee:
    def __init__(self, elements):
        self.n = 0
        self.first = None
        self.last = None
        if elements:
            for e in elements:
                self.insert_last(e)
        
    def __repr__(self):
        return repr(self.first)
    
    def insert_first(self, data):
        self.first = Node(data, self.first)
        if self.last is None:
            self.last = self.first
        self.n += 1
        
    def insert_last(self, data):
        if self.last is None:
            self.first = self.last = Node(data)
        else:
            self.last.next = Node(data)
            self.last = self.last.next
        self.n += 1    
        
    def get_first(self):
        if self.first is None:
            raise ValueError('Structure is empty')
        return self.first.data

    def remove_first(self):
        if self.first is None:
            raise ValueError('Structure is empty')
        data = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        self.n -= 1
        return data
    
    def __len__(self):
        return self.n
    
    def __contains__(self, data):
        p = self.first
        while p is not None:
            if p.data == data:
                return True
            p = p.next
        return False

class Pile(ListeChainee):
    def __init__(self):
        super().__init__()
        self.max_str = 0
        
    def push(self, data):
        self.insert_first(data)
        self.max_str = max(self.max_str,len(str(data))) 
        
    def pop(self):
        return self.remove_first()
    
    def get_top(self):
        return self.get_first()
    
    def __str__(self):
        res = ''
        p = self.first
        while p is not None:
            res += "|" + str(p.data).center(self.max_str+2) + "|\n"
            p = p.next
        res += '-' * (self.max_str+4)
        return res
        
class File(ListeChainee):
    def __init__(self):
        super().__init__()
        
    def insert(self, data):
        self.insert_last(data)
        
    def remove(self):
        return self.remove_first()
    
    def __str__(self):
        res = ''
        p = self.first
        while p is not None:
            res += str(p.data) + " <- "
            p = p.next
        res = res[:-4] # pour retirer la dernière flèche
        return res    
        


test = ListeChainee([1, 2, 3, 4, 5])
print(test)
