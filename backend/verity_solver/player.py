from shape import Shape
from typing import Optional

class Player:
    def __init__(self, anchor: Shape, s1: Shape, s2: Shape):
        self.anchor = anchor
        self.s1 = s1
        self.s2 = s2

    def contains(self, shape: Shape) -> bool:
        return self.anchor == shape or self.s1 == shape or self.s2 == shape
    
    def is_complete(self) -> bool:
        return len({self.anchor, self.s1, self.s2}) == 3

    def duplicate_shape(self) -> Optional[Shape]:
        seen = set()
        seen.add(self.anchor)

        if self.s1 in seen:
            return self.s1
        else:
            seen.add(self.s1)
        
        if self.s2 in seen:
            return self.s2
        
        return None
    
    def swap(self, old_shape: Shape, new_shape: Shape):
        if self.s1 == old_shape:
            self.s1 = new_shape
        elif self.s2 == old_shape:
            self.s2 = new_shape