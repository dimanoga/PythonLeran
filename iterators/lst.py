class DoubleeleentListIterator:
    def __init__(self,lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i -2],self.lst[self.i -1]
        else:
            raise StopIteration

class Mylist(list):
    def __iter__(self):
        return DoubleeleentListIterator(self)

for pair in Mylist([1,2,3,4]):
    print(pair)
