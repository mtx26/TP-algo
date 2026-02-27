
class PileTriee():
    def __init__(self, n=0, reversed=False):
        self.disk = []
        self.reversed = reversed
        for i in range(n):
            if reversed:
                a = i + 1
            else:
                a = n - i
            self.disk.append(a)
            
    def __str__(self):
        return str(self.disk)
    
    def __repr__(self):
        return self.disk
    
    def is_null(self):
        return self.disk == []
    
    def get_last(self):
        return self.disk[-1]
            
    def add_disk(self, i):
        
        if self.disk:
            if (self.get_last() > i) == (not self.reversed):
                self.disk.append(i)
            else:
                raise AssertionError("Imposible d'ajouter element")
        else:
            self.disk.append(i)
        
    def remove_disk(self):
        if self.disk:
            return self.disk.pop()
        else:
            raise IndexError("pile vide")
        
class HanoiTowers():
    def __init__(self):
        self.tower_1 = PileTriee(3)
        self.tower_2 = PileTriee()
        self.tower_3 = PileTriee()
    
    def __str__(self):
        return str(self.tower_1) + " - " + str(self.tower_2) + " - " + str(self.tower_3)
    
    def moveDisk(self, origin: PileTriee, end: PileTriee):
        if origin.is_null():
            raise IndexError("pile vide")
        else:
            end.add_disk(origin.remove_disk())
    
    def check_win(self):
        return self.tower_1.is_null() and self.tower_2.is_null()
        
    
test = HanoiTowers()
print(test)
test.moveDisk(test.tower_1, test.tower_3)
print(test)
test.moveDisk(test.tower_1, test.tower_2)
print(test)
test.moveDisk(test.tower_3, test.tower_2)
print(test)
test.moveDisk(test.tower_1, test.tower_3)
print(test)
test.moveDisk(test.tower_2, test.tower_1)
print(test)
test.moveDisk(test.tower_2, test.tower_3)
print(test)
test.moveDisk(test.tower_1, test.tower_3)
print(test)
print(test.check_win())
        
        
        