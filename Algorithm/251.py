#251. Flatten 2D Vector:
class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.inner = 0 
        self.outer = 0

    def advanceToNext(self):
        while self.outer < len(self.vector) and self.inner == len(self.vector[self.outer]):
        	self.outer += 1
        	self.inner = 0

    def next(self) -> int:
        self.advanceToNext()
        result = self.vector[self.outer][self.inner]
        self.inner += 1
        return result

    def hasNext(self) -> bool:
        self.advanceToNext()
        return self.outer < len(self.vector)

#self.advanceToNext: goes through all of the possible missing elements.

self.vec = vec 
self.inner = 0
self.outer = 0


self.advanceToNext()
result = self.vector[self.outer][self.inner]
self.inner += 1
-> advance the element to the next position there


